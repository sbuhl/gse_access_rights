# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountJournal(models.Model):
    _inherit = "account.journal"

    sbu_allowed_user_ids = fields.Many2many("res.users", string="Allowed Users")

