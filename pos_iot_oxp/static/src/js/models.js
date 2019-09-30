odoo.define('pos_iot_oxp.models', function (require) {
    "use strict";

    var models = require("point_of_sale.models");
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
                    identifier: iot_device.identifier
                });
            }
        },
    });

    var posmodel_super = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        after_load_server_data: function() {
            posmodel_super.after_load_server_data.apply(this, arguments).then(function () {
                self.keyboard.add_listener(self._onKeyPressed.bind(self));
            });
        },
        _onKeyPressed: function(data) {
            console.log(data.value);
        }
    })
});

