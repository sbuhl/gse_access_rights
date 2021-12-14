# -*- coding: utf-8 -*-

{
    'name': "access_rights",
    'version': '0.1',
    'depends': ['base', 'l10n_be', 'sale', 'stock'],
    
    'author': "Sébastien Bühl",
    'website': "http://www.buhl.be",
    'license': 'LGPL-3',

    'application': True,
    'category': 'Other Extra Rights',
    'summary': 'Allow access to other user documents',
    'description': """
        Access rights for invoices and other stuffs.
    """,

    'data': [
        'security/security.xml',
        'views/res_users.xml',
        'views/account_move.xml',
    ],
}
