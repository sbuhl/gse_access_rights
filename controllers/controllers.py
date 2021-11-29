# -*- coding: utf-8 -*-
# from odoo import http


# class AccessRights(http.Controller):
#     @http.route('/access_rights/access_rights/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/access_rights/access_rights/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('access_rights.listing', {
#             'root': '/access_rights/access_rights',
#             'objects': http.request.env['access_rights.access_rights'].search([]),
#         })

#     @http.route('/access_rights/access_rights/objects/<model("access_rights.access_rights"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('access_rights.object', {
#             'object': obj
#         })
