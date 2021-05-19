# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json
# import datetime

class Modsergio(http.Controller):
    @http.route('/api/sendPass/', auth='public')
    def sendPass(self, **kw):
        # self.env['res.users'].sudo().search([('id','=','12')])[0].action_reset_password()
        try:
            self.sudo(user=12).action_reset_password()
            usuario = http.request.env['res.users'].sudo().search([('id','=','12')])[0] #.sudo().action_reset_password()
            #usuario.action_reset_password()
            return Response(json.dumps({'result': 'sended', 'usuario':str(usuario)}), content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
        #records.action_reset_password()
        #return "Intentaremos enviar el reset de pass"

    @http.route('/api/usuarios', auth='public', method=['GET'], csrf=False)
    def get_usuarios(self, **kw):
        try:
            usuarios = http.request.env['res.users'].sudo().search_read([], ['name', 'email'])
            res = json.dumps(usuarios, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

#     @http.route('/modsergio/modsergio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modsergio.listing', {
#             'root': '/modsergio/modsergio',
#             'objects': http.request.env['modsergio.modsergio'].search([]),
#         })

#     @http.route('/modsergio/modsergio/objects/<model("modsergio.modsergio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modsergio.object', {
#             'object': obj
#         })
