# -*- coding: utf-8 -*-
from odoo import http


class Modsergio(http.Controller):
    @http.route('/api/sendPass/', auth='public')
    def index(self, **kw):
        return "Intentaremos enviar el reset de pass"

#     @http.route('/modsergio/modsergio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modsergio.listing', {
#             'root': '/modsergio/modsergio',
#             'objects': http.request.env['modsergio.modsergio'].search([]),
#         })

#     @http.route('/modsergio/modsergio/objects/<model("modsergio.modsergio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modsergio.object', {
#             'object': obj
#         })
