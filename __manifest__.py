# -*- coding: utf-8 -*-
{
    'name': "Hotel manegment system",

    'description': "HMS made easy",

    'author': "Merit",
    'category': 'HMS',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/views.xml',

    ],
    # only loaded in demonstration mode

}
