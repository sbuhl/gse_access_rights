# -*- coding: utf-8 -*-

from odoo import http, models, fields, api


class Users(models.Model):
    
    _inherit = 'res.users'

    sbu_allowed_users_ids = fields.Many2many(comodel_name='res.users', relation="sbu_allowed_users_rel", column1="left_user_id", column2="right_user_id", string="Allowed Users")  # noqa: E501
    sbu_allowed_warehouses_ids = fields.Many2many(comodel_name='stock.warehouse', relation="sbu_allowed_warehouses_rel", column1="res_user_id", column2="stock_warehouse_id", store=True)  # noqa: E501
    journal_ids = fields.Many2many('account.journal', string="Allowed Journals")  # noqa: E501
