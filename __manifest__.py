# -*- coding: utf-8 -*-
{
    'name': "website_event_snippet",

    'summary': """
        This module sorts the events in the event snippet dynamic block ascending
    """,

    'description': """
        This module sorts the events in the event snippet dynamic block ascending
    """,

    'author': "Seppe De Loore",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '16.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['website_event'],

    # always loaded
    'data': [
        'data/website_snippet_data.xml',
    ],
}
