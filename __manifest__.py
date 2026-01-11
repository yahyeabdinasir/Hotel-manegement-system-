# -*- coding: utf-8 -*-
{
    'name': "Hotel manegment system",

    'description': "HMS made easy",
    'sequence': 103,

    'author': "Merit",
    'category': 'HMS',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/customer_sequence.xml',
         # 'views/menu_view.xml',
        'views/views.xml',
        'views/rooms.xml',
    ],
    # only loaded in demonstration mode

}
