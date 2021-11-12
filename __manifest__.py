# -*- coding: utf-8 -*-
{
    'name': "Analisis Investor",
    'summary': 'Module Odoo melakukan analisis investor.',
    'description': 'Module Odoo untuk melakukan analisis investor pada suatu perusahaan beradasarkan omzet, daya bayar, dana kesehatan keuangan.',
    'sequence': -100,
    'author': "apaya.id",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cats_menus.xml',
        'views/cats_trees.xml',
        'views/cats_forms.xml',
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
