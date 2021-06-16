# -*- coding: utf-8 -*-
from odoo import http

# class MethodPosNotaCombo(http.Controller):
#     @http.route('/method_pos_nota_combo/method_pos_nota_combo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_pos_nota_combo/method_pos_nota_combo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_pos_nota_combo.listing', {
#             'root': '/method_pos_nota_combo/method_pos_nota_combo',
#             'objects': http.request.env['method_pos_nota_combo.method_pos_nota_combo'].search([]),
#         })

#     @http.route('/method_pos_nota_combo/method_pos_nota_combo/objects/<model("method_pos_nota_combo.method_pos_nota_combo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_pos_nota_combo.object', {
#             'object': obj
#         })