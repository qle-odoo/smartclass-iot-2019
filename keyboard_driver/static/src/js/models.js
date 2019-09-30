odoo.define('pos_iot_oxp_models', function(require){
    'use strict';

    var models = require('point_of_sale.models');
    var DeviceProxy = require('iot.widgets').DeviceProxy;

    //load models
    models.load_models({
        model: 'iot.device',
        fields: ['iot_ip', 'identifier', 'type'],
        domain: function(self){
            return [['id', '=', self.config.iot_keyboard_id[0]]]
        },
        loaded: function(self, iot_devices){//if loaded successfully, get the device
            if(iot_devices){
                var iot_device = iot_devices[0];
                self.keyboard = new DeviceProxy({
                    iot_ip:  iot_device.iot_ip,
                    identifier: iot_device.identifier
                })
            }
        }
    })

    var posmodel_super = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({

        after_load_server_data: function () {
            var self = this;
            return posmodel_super.after_load_server_data.apply(this, arguments)
                .then(function () {
                    self.keyboard.add_listener(self._onKeyPressed.bind(self));
                });
        },

        _onKeyPressed: function (data) {
            var input = $('.searchbox input')[0];
            if(input){
                input.dispatchEvent(new KeyboardEvent('keypress', {char: data.value}));
                if(data.value == "BACKSPACE"){
                    input.value = input.value.slice(0, -1);
                }else{
                    input.value += data.value
                }
                input.dispatchEvent(new KeyboardEvent('keyup', {char: data.value}));
            }
        }
    });
})