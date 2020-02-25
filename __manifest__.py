# -*- coding: utf-8 -*-
{
    'name': "IT Devices",
    'summary': """Devices inventory for IT helpdesk
        """,
    'website': "https://github.com/kmcalda/it-monitoring.git",
    'author': "Kevin Marvin Calda",
    'category': 'Tool',
    'version': '0.1',
    'license': 'AGPL-3',
    'depends': ['base','mail'],
    'data': [
        'views/laptops.xml',
        'views/desktops.xml',
        'views/printers.xml',
    ],
    'application': True,
    'installation': True,
    'auto_install': False,
}