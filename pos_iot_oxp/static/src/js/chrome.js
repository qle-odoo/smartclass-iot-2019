odoo.define('pos_iot_oxp.chrome', function (require) {
    "use.strict";
    
    var chrome = require('point_of_sale.chrome');
    
    chrome.Chrome.include({
        keyboard_light_button_widget: {
            'name': 'keyboard_light_button',
            'widget': chrome.HeaderButtonWidget,
            'append': '.pos-rightheader',
            'args': {
                'label': 'Change All Keyboard LEDs',
                'action': function () {
                    this.pos.keyboard.action({
                        'action': 'change_all_led',
                    });
                }
            },
        },
    
        build_widgets: function () {
            if (this.pos.keyboard) {
                this.widgets.push(this.keyboard_light_button_widget);
            }
            this._super();
        }
    });


    chrome.Chrome.include({
        keyboard_button_widget: {
            'name': 'keyboard_button',
            'widget': chrome.HeaderButtonWidget,
            'append': '.pos-rightheader',
            'args': {
                'label': 'Change Left Keyboard LED',
                'action': function () {
                    this.pos.keyboard.action({
                        'action': 'change_led',
                    });
                }
            },
        },
    
        build_widgets: function () {
            if (this.pos.keyboard) {
                this.widgets.push(this.keyboard_button_widget);
            }
            this._super();
        }
    });

   
    
    });