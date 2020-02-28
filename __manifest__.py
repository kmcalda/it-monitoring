# -*- coding: utf-8 -*-
{
    'name': "Devices",
    'summary': """Devices inventory for IT helpdesk
        """,
    'website': "https://github.com/kmcalda/it-monitoring.git",
    'author': "Kevin Marvin Calda",
    'category': 'Tool',
    'version': '0.1',
    'license': 'AGPL-3',
    'depends': ['base','mail'],
    'data': [
        'views/devices.xml',
        'views/laptops.xml',
        'views/desktops.xml',
        'views/printers.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installation': True,
    'auto_install': False,
}