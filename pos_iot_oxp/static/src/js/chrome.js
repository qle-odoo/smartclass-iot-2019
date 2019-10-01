odoo.define('pos_iot_oxp.chrome', function (require) {
"use.strict";

var chrome = require('point_of_sale.chrome');

chrome.Chrome.include({
    keyboard_numlock_button_widget: {
        'name': 'keyboard_numlock_button',
        'widget': chrome.HeaderButtonWidget,
        'append': '.pos-rightheader',
        'args': {
            'label': 'Change keyboard numlock led',
            'action': function () {
                this.pos.keyboard.action({
                    'action': 'change_numlock_led',
                });
            }
        },
    },
    keyboard_capslock_button_widget: {
        'name': 'keyboard_capslock_button',
        'widget': chrome.HeaderButtonWidget,
        'append': '.pos-rightheader',
        'args': {
            'label': 'Change keyboard capslock led',
            'action': function () {
                this.pos.keyboard.action({
                    'action': 'change_capslock_led',
                });
            }
        },
    },


    build_widgets: function () {
        if (this.pos.keyboard) {
            this.widgets.push(this.keyboard_numlock_button_widget);
            this.widgets.push(this.keyboard_capslock_button_widget);
        }
        this._super();
    }
});

});
