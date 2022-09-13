# -*- coding: utf-8 -*-

from odoo import models, fields


class Users(models.Model):
    
    _inherit = 'res.users'

    sbu_allowed_users_ids = fields.Many2many(
        comodel_name='res.users', 
        relation="sbu_allowed_users_rel", 
        column1="left_user_id", 
        column2="right_user_id", 
        string="Allowed Users", 
        domain=['|', ('active', '=', True), ('active', '=', False)],
        context={'active_test': False},
    )
    sbu_allowed_warehouses_ids = fields.Many2many(
        comodel_name='stock.warehouse', 
        relation="sbu_allowed_warehouses_rel", 
        column1="res_user_id", 
        column2="stock_warehouse_id", 
        string="Allowed Warehouse", 
        store=True,
    )
    journal_ids = fields.Many2many(
        'account.journal', 
        string="Allowed Journals",
    )
