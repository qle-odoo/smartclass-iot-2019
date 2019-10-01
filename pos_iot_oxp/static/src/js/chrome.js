odoo.define('pos_iot_oxp.chrome', function (require) {
"use.strict";

var chrome = require('point_of_sale.chrome');

chrome.Chrome.include({
    keyboard_button_widget: {
        'name': 'keyboard_button',
        'widget': chrome.HeaderButtonWidget,
        'append': '.pos-rightheader',
        'args':{
            'label': 'Change Keyboard LED',
            'action': function () {
                this.pos.iot_device_proxies.keyboard.action({
                    'action': 'change_led',
                });
            }
        },
    },

    build_widgets: function () {
        if (this.pos.iot_device_proxies.keyboard) {
            this.widgets.push(this.keyboard_button_widget);
        }
        this._super();
    }

});

});