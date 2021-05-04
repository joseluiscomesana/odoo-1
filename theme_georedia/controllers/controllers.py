# -*- coding: utf-8 -*-
from odoo import http
import json

class ThemeGeoredia(http.Controller):
    @http.route('/web/prueba1', auth='public')
    def index(self, **kw):
        return "Hello, world - " + http.request.params['nombre']


    # @http.route('/web/prueba2', type='http', csrf=False, auth="public")
    # def update_order_webhook(self, **kwargs):
    #     return Response(json.dumps({"yes":"i am json"}),content_type='application/json;charset=utf-8',status=200)


    @http.route('/web/prueba3', type='json', auth="public", website=True)
    def update_order_webhook(self, **kwargs):
        return json.dumps({"yes":"i am json"})
    
    @http.route('/web/prueba4', auth='none', type="json", methods=['GET'], csrf=False, cors='*')
    def index(self, **kw):
        data = json.loads(http.request.httprequest.data) # I need raw data
        return data

# import requests

# url = "https://dev-expert.snippetbucket.com/api/get_user_information/"


# headers = {
#     'content-type': "application/json",
#     'user-token': "02BXD2AGqVH-TEJASTANK-gg92DwntD8f1p0tb",
#     'cache-control': "no-cache",
#     }
# payload = "{\"params\": {}}"
# response = requests.request("GET", url, data=payload, headers=headers)

# print(response.text)