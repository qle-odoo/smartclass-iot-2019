odoo.define('pos_iot_oxp.models', function (require) {
"use strict";

var models = require('point_of_sale.models');

models.load_models({
   model: 'iot_device',
   fields: ['iot_ip', 'identifier', 'type'],
   domain: function (self) {
       return [['id', '=', self.config.iot_keyboard_id[0]]]
   },
   loaded: function (self, iot_devices) {
        if (iot_devices) {
            var iot_device = iot_devices[0];
            self.keyboard = new DeviceProxy({
                iot_ip: iot_device.identifier,
                identifier: iot_device.identifier,
            });
        }
   },
 });
});
