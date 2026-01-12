# -*- coding: utf-8 -*-
{
    'name': "Hotel manegment system",

    'description': "HMS made easy",
    'sequence': 120,

    'author': "Merit",
    'category': 'HMS',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/customer_sequence.xml',
        'data/booking_sequence.xml',

         'views/menu_view.xml',
        'views/views.xml',
        'views/rooms.xml',
        'views/boooking.xml',
    ],
    # only loaded in demonstration mode

}
