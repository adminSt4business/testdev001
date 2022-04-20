# _*_ coding: utf-8 _*_
{
    'name': 'Odoo Acamedy',
    'Sumary': """Academy app to manage Training""",
    'description': """
       Academy Module to manage Training
       + Courses
       + Sessions
       + Atendees
    """,
    'author': 'JPrieto',
    'website': 'https://www.st4business.com',
    'license': 'GNU LGPL v3',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
    ],
    'demo':[
        'demo/academy_demo.xml'
    ],
}