# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'pos_iot_oxp',
    'version': '1.0',
    'category': 'Sales/Point Of Sale',
    'sequence': 6,
    'summary': 'Control the POS with IoT-Box Keyboard',
    'description': """

""",
    'data': [
        'views/pos_config_views.xml',
    ],
    'depends': ['pos_iot'],
    'installable': True,
}
