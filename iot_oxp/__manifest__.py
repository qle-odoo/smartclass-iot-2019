# -*- coding: utf-8 -*-
{
    'name': 'IoT OXP Exercise',

    'summary': '''Custom IoT App''',

    'description': '''
Custom IoT App
=


    ''',
    'author': 'Odoo, Inc',
    'website': 'https://www.odoo.com',
    'category': 'IoT',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [
        'iot'
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}