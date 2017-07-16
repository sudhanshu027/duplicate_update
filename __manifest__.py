# -*- coding: utf-8 -*-
{
    'name': "Duplicate Update",

    'summary': """
        To duplicate without save.""",

    'description': """
        To duplicate a record without creating a record at the backend.
    """,

    'author': "Navyug Infosolutions",
    'website': "http://www.navyuginfo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/resources.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
