# -*- coding: utf-8 -*-
{
    'name': "Analisis Investor",
    'summary': 'Module Odoo untuk menyimpan data investor.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan data Investor',
    'sequence': -100,
    'author': "Pluang.id",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/investors_menus.xml',
        'views/investors_trees.xml',
        'views/investors_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
