# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'pos_iot_oxp',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Use a keyboard connected to an IoT Box in your Point of Sale',
    'description': """
Connect a keyboard to your IoT Box and use it in your Point of Sale to search products.
""",
    'depends': ['pos_iot'],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
