odoo.define('keyboard_driver.chrome', function (require) {
    "use.strict";
    
    var chrome = require('point_of_sale.chrome');
    
    chrome.Chrome.include({
        keyboard_button_widget: {
            'name': 'keyboard_button',
            'widget': chrome.HeaderButtonWidget,
            'append': '.pos-rightheader',
            'args': {
                'label': 'Change keyboard led',
                'action': function () {
                    this.pos.keyboard.action({
                        'action': 'change_led',
                    });
                }
            },
        },
        keyboard_caps_button_widget: {
            'name': 'keyboard_caps_button',
            'widget': chrome.HeaderButtonWidget,
            'append': '.pos-rightheader',
            'args': {
                'label': 'Change Caps Lock led',
                'action': function () {
                    this.pos.keyboard.action({
                        'action': 'change_caps',
                    });
                }
            },
        },
    
        build_widgets: function () {
            if (this.pos.keyboard) {
                this.widgets.push(this.keyboard_button_widget);
                this.widgets.push(this.keyboard_caps_button_widget);
            }
            this._super();
        }
    });
    
    });