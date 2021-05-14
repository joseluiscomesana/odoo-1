# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json
import datetime

class PresupuestosController(http.Controller):
    # Datos de un articulo por su id o por su código 
    @http.route('/api/presupuestos/busca/<obj>/', auth='public',website=True)
    def object_pre(self, obj, **kw):
        try:
            def fecha(o):
                if isinstance(o,datetime.datetime):
                    return "{}-{}-{}".format(o.year, o.month, o.day)
            try:
                int(obj)
                busca = 'id'
            except ValueError:
                busca = 'ensayo'
            condicion = [(busca,'=',obj)] 
            presupuestos = http.request.env['presupuestos.presupuesto'].sudo().search_read(condicion)
           # res = json.dumps(presupuestos,default=fecha).encode('utf-8')
            return http.request.render('presupuestos.index2',{
                'objects':presupuestos
            })
            # return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/presupuestos/lt', auth='public',method=['GET'],website=True)
    def index(self, **kw):
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
    
    # Datos de un articulo por su id o por su código 
    @http.route('/api/articulo/buscar/<obj>/', auth='public')
    def object_art(self, obj, **kw):
        try:
            def fecha(o):
                if isinstance(o,datetime.datetime):
                    return "{}-{}-{}".format(o.year, o.month, o.day)
            try:
                int(obj)
                condicion =[('id','=',obj)] 
            except ValueError:
                condicion = [('name','like','%'+obj+'%')] 
            campos =['id','name','description','categ_id','currency_id','price'] 
            presupuestos = http.request.env['product.template'].sudo().search_read(condicion,campos)
            res = json.dumps(presupuestos,default=fecha).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    @http.route('/api/articulos/lt', auth='public',method=['GET'],website=True)
    def index_tot(self, **kw):
        artis = http.request.env['product.template']
        return http.request.render('presupuestos.articulos',{
            'objects':artis.search([])
        })

