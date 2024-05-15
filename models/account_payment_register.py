# -*- coding: utf-8 -*-

from odoo import api, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    @api.model
    def _get_batch_available_journals(self, batch_result):
        return super(
            AccountPaymentRegister,
            self.with_user(self.env.user),
        )._get_batch_available_journals(batch_result)
