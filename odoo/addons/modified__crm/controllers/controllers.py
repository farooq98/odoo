# -*- coding: utf-8 -*-
# from odoo import http


# class ModifiedCrm(http.Controller):
#     @http.route('/modified__crm/modified__crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modified__crm/modified__crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modified__crm.listing', {
#             'root': '/modified__crm/modified__crm',
#             'objects': http.request.env['modified__crm.modified__crm'].search([]),
#         })

#     @http.route('/modified__crm/modified__crm/objects/<model("modified__crm.modified__crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modified__crm.object', {
#             'object': obj
#         })
