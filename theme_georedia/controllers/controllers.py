# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/api/prueba1', auth='public')
    def index(self, **kw):
        return "Hello, world - " + http.request.params['nombre']


    @http.route('/api/prueba2', type='http', csrf=False, auth="public")
    def update_order_webhook(self, **kwargs):
        return Response(json.dumps({"yes":"i am json"}),content_type='application/json;charset=utf-8',status=200)