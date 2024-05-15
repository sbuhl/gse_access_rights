# -*- coding: utf-8 -*-

from odoo import models, fields


class Users(models.Model):
    _name = 'res.users'
    _inherit = [
        'res.users',
        'mail.thread',  # add chatter capability
    ]

    sbu_allowed_users_ids = fields.Many2many(
        comodel_name='res.users',
        relation="sbu_allowed_users_rel",
        column1="left_user_id",
        column2="right_user_id",
        string="Allowed Users",
        domain=['|', ('active', '=', True), ('active', '=', False)],
        context={'active_test': False},
    )
    sbu_allowed_user_ids_inverse = fields.Many2many(
        comodel_name='res.users',
        relation="sbu_allowed_users_rel",
        column1="right_user_id",
        column2="left_user_id",
        string="Users Allowed",
    )
    sbu_allowed_warehouses_ids = fields.Many2many('stock.warehouse', string="Allowed Warehouse")
    journal_ids = fields.Many2many('account.journal', string="Allowed Journals")

    def write(self, values):
        autor = self.env.user.name
        user_groups = {}
        to_track = [
            'groups_id',
            'sbu_allowed_users_ids',
            'sbu_allowed_warehouses_ids',
            'journal_ids',
        ]
        for user in self:
            user_groups[user] = {}
            for field in to_track:
                user_groups[user][field] = user[field]

        res = super().write(values)

        for user in self:
            body = []
            for field in to_track:
                previous_values = user_groups[user][field]
                new_values = user[field] - previous_values
                removed_values = previous_values - user[field]
                if new_values:
                    body.append(f"- a ajouté l'accès à [{len(new_values)} {new_values._description}] : {new_values.mapped('display_name')}")
                if removed_values:
                    body.append(f"- a retiré l'accès à [{len(removed_values)} {removed_values._description}] : {removed_values.mapped('display_name')}")
            if body:
                body.insert(0, autor)
                user.message_post(body='<br>'.join(body))

        return res