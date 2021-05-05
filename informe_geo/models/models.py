# -*- coding: utf-8 -*-

from odoo import models, fields, api
# import datetime

class informe(models.Model):
    _name = 'informe_geo.informe'
    _description = 'Informe'

    name = fields.Char(string='Nombre')
    filename = fields.Char(string='Fichero')
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string='Descripción')
    file_data = fields.Binary('Archivo')
    file_name = fields.Char('Nombre archivo')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
