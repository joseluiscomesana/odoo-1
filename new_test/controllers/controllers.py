# -*- coding: utf-8 -*-
# from odoo import http


# class NewTest(http.Controller):
#     @http.route('/new_test/new_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_test/new_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_test.listing', {
#             'root': '/new_test/new_test',
#             'objects': http.request.env['new_test.new_test'].search([]),
#         })

#     @http.route('/new_test/new_test/objects/<model("new_test.new_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_test.object', {
#             'object': obj
#         })
