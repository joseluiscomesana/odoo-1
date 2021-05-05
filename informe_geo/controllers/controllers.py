# -*- coding: utf-8 -*-
from odoo import http
# from http import request
import json


class InformeGeo(http.Controller):
    @http.route('/apiweb/', auth='public', type="json", methods=['GET'], csrf=False, cors='*')
    def index(self, **kw):
        data = json.loads(http.request.httprequest.data) # I need raw data
        return data



    @http.route('/informe_geo/informe_geo/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/informe_geo/informe_geo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('informe_geo.listing', {
#             'root': '/informe_geo/informe_geo',
#             'objects': http.request.env['informe_geo.informe_geo'].search([]),
#         })

#     @http.route('/informe_geo/informe_geo/objects/<model("informe_geo.informe_geo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('informe_geo.object', {
#             'object': obj
#         })
