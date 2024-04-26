# -*- coding: utf-8 -*-

from odoo import models, fields


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    sbu_allowed_user_ids = fields.Many2many("res.users", string="Allowed Users")
