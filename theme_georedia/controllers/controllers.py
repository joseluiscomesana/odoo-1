# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/api/prueba/', auth='public')
    def index(self, **kw):
        return "Hello, world - " + http.request.params['nombre']