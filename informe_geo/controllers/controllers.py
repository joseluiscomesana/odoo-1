# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import response
import json


class InformeController(http.Controller):
    @http.route('/apiweb/', auth='public', type="json", methods=['GET'], csrf=False, cors='*')
    def index(self, **kw):
        data = json.loads(http.request.httprequest.data) # I need raw data
        return data



    @http.route('/informe_geo/informe_geo/', auth='public')
    def index(self, **kw):
        return "Hello, world"


    # @http.route('/api/indormes', auth='public', method=['GET'], csrf=False)
    # def get_indormes(self, **kw):
    #     try:
    #         indormes = http.request.env['informe_geo.informe'].sudo().search_read([], ['id', 'name', 'description', 'file_name'])
    #         res = json.dumps(indormes, ensure_ascii=False).encode('utf-8')
    #         return response(res, content_type='application/json;charset=utf-8', status=200)
    #     except Exception as e:
    #         return response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)



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
