# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):

    _inherit = 'account.move'

    invoice_payment_wigdet_journal = fields.Char(string="Invoice Payments", compute="_get_payment_widget")

    @api.depends('move_type', 'line_ids.amount_residual')
    def _get_payment_widget(self):
        for record in self:
            record.sudo()._compute_payments_widget_reconciled_info()
            record['invoice_payment_wigdet_journal'] = record.invoice_payments_widget

    # === Payment widget fields === #
    invoice_outstanding_credits_debits_widget = fields.Binary(
        groups="account.group_account_manager",
        compute='_compute_payments_widget_to_reconcile_info',
        exportable=False,
    )
    invoice_has_outstanding = fields.Boolean(
        groups="account.group_account_manager",
        compute='_compute_payments_widget_to_reconcile_info',
    )
    invoice_payments_widget = fields.Binary(
        groups="account.group_account_manager",
        compute='_compute_payments_widget_reconciled_info',
        exportable=False,
    )
