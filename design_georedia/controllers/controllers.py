# -*- coding: utf-8 -*-
from odoo import http


class DesignGeoredia(http.Controller):
    @http.route('/design_georedia/design_georedia/', auth='public')
    def index(self, **kw):
        return http.request.render('design_georedia.index', {})

#     @http.route('/design_georedia/design_georedia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('design_georedia.listing', {
#             'root': '/design_georedia/design_georedia',
#             'objects': http.request.env['design_georedia.design_georedia'].search([]),
#         })

#     @http.route('/design_georedia/design_georedia/objects/<model("design_georedia.design_georedia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('design_georedia.object', {
#             'object': obj
#         })
