odoo.define('pos_iot_oxp.chrome', function (require) {
"use strict";

var chrome = require('point_of_sale.chrome');
var core = require('web.core');

var _t = core._t;

chrome.Chrome.include({
    keyboard_button_widget: {
        'name': 'keyboard_button',
        'widget': chrome.HeaderButtonWidget,
        'append': '.pos-rightheader',
        'args': {
            label: _t('Change Keyboard Led'),
            action: function () {
                this.pos.iot_device_proxies.keyboard.action({ action: 'change_led_status' });
            }
        }
    },

    build_widgets: function () {
        if (this.pos.config.iot_keyboard_id) {
            // Place it left to the Close button
            var close_button_index = _.findIndex(this.widgets, function (widget) {
                return widget.name === "close_button";
            });
            this.widgets.splice(close_button_index, 0, this.keyboard_button_widget);
        }
        this._super();
    },
});


});
