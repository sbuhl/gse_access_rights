# -*- coding: utf-8 -*-

{
    'name': "Access Rigths",
    'version': '0.8.2',
    'depends': [
        'base', 'hr', 'l10n_be', 'account', 'account_accountant', 'sale', 'stock', 'partner_commission', 'industry_fsm',
        'industry_fsm_sale_report',
        'account_approval',  # account_approval.group_sales_level_manager
    ],
    'description': """
    Allow to specify access rights on users, journals and warehouses.
    """,
    'author': "Sébastien Bühl",
    'website': "https://github.com/sbuhl/gse_access_rights",
    'license': 'LGPL-3',

    'application': True,
    'category': 'Customizations',
    'summary': 'Allow access to other user documents',

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_users.xml',
        'views/account_bank_statement.xml',
        'views/account_move.xml',
        'views/check_access.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/project_task.xml',
        'views/account_menu.xml',

    ],
}
