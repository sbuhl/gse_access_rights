# -*- coding: utf-8 -*-

from odoo import models, fields


class StockLocation(models.Model):
    _inherit = 'stock.location'

    sbu_allowed_warehouses_id = fields.Many2one(comodel_name='stock.warehouse', store=True)  # noqa: E501