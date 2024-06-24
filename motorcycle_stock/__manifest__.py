# -*- coding: utf-8 -*-
{
    'name': "motorcycle_stock",


    'author': "webilityGit",
    'website': "https://github.com/webilityGit/tech_training",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Kawiil/Custom Modules',
    'version': '0.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['motorcycle_registry', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/stock_menu.xml',
        'views/product_template_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto-install': True,
}
