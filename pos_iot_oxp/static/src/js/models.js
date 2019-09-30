odoo.define('pos_iot_oxp.models', function (require) {
"use strict";

var models = require('point_of_sale.models');
var DeviceProxy = require('iot.widgets').DeviceProxy;

models.load_models({
    model: 'iot.device',
    fields: ['iot_ip', 'identifier', 'type'],
    domain: function (self) {
        return [['id', '=', self.config.iot_keyboard_id[0]]];
    },
    loaded: function (self, iot_devices) {
        if (iot_devices) {
            var iot_device = iot_devices[0];
            self.keyboard = new DeviceProxy({
                iot_ip: iot_device.iot_ip,
                identifier: iot_device.identifier,
            });
        }
    },
});

});