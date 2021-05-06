# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class VisitController(http.Controller):

    @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
    def get_visits(self, **kw):
        try:
            visits = http.request.env['prueba.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

class ControllerVisit(http.Controller):

    @http.route('/api/visit', auth='public', method=['GET'], csrf=False)
    def get_visits(self, **kw):
        try:
            visits = http.request.env['prueba.ir.act.window'].sudo().search_read([], ['id', 'name', 'type', 'res_model'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return http.request.render('prueba.index',visits)
            # Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class Prueba(http.Controller):
    @http.route('/prueba/prueba/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/prueba/prueba/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('prueba.listing', {
            'root': '/prueba/prueba',
            'objects': http.request.env['prueba.prueba'].search([]),
        })

#     @http.route('/prueba/prueba/objects/<model("prueba.prueba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba.object', {
#             'object': obj
#         })
