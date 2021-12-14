# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):

    _inherit = 'account.move'

    invoice_payment_wigdet_journal = fields.Char(string="Payments", compute="_get_payment_widget")

    @api.depends('move_type', 'line_ids.amount_residual')
    def _get_payment_widget(self):
        for record in self:
            record.sudo()._compute_payments_widget_reconciled_info()
            record['invoice_payment_wigdet_journal'] = record.invoice_payments_widget
