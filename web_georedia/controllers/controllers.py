# -*- coding: utf-8 -*-
# from odoo import http


# class WebGeoredia(http.Controller):
#     @http.route('/web_georedia/web_georedia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_georedia/web_georedia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_georedia.listing', {
#             'root': '/web_georedia/web_georedia',
#             'objects': http.request.env['web_georedia.web_georedia'].search([]),
#         })

#     @http.route('/web_georedia/web_georedia/objects/<model("web_georedia.web_georedia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_georedia.object', {
#             'object': obj
#         })
