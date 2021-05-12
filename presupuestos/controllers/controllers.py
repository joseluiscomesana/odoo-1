# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class PresupuestosController(http.Controller):
    @http.route('/api/presupuestos/lt', auth='public',method=['GET'],website=True)
    def index(self, **kw):
#        return '<h1>Aqui llega bien</h1>'
        presus = http.request.env['presupuestos.presupuesto']
        return http.request.render('presupuestos.index',{
            'objects':presus.search([])
        })
    @http.route('/api/presupuestos', auth='public', method=['GET'], csrf=False)
    def get_presupuestos(self, **kw):
        try:
            presupuestos = http.request.env['presupuestos.presupuesto'].sudo().search_read([], ['id', 'ensayo', 'descripcion'])
            res = json.dumps(presupuestos, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

# class Presupuestos(http.Controller):
#     @http.route('/presupuestos/presupuestos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/presupuestos/presupuestos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('presupuestos.listing', {
#             'root': '/presupuestos/presupuestos',
#             'objects': http.request.env['presupuestos.presupuestos'].search([]),
#         })

#     @http.route('/presupuestos/presupuestos/objects/<model("presupuestos.presupuestos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('presupuestos.object', {
#             'object': obj
#         })
