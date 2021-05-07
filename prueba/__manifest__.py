# -*- coding: utf-8 -*-
{
    'name': "prueba",

    'summary': """
        Aplicación de prueba para comprobar el funcionamiento
        de los módulos""",

    'description': """
        Sólo con propósitos de prueba
    """,

    'author': "Jfic",
    'website': "http://www.georedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.12',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/visit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
