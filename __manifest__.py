# -*- coding: utf-8 -*-
{
    'name': "method_pos_nota_combo",

    'summary': """
        Agrega como nota los ingredientes del combo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Method ERP SpA",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','aspl_pos_combo'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}