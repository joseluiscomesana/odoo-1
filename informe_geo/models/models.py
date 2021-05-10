# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class informe_geo(models.Model):
#     _name = 'informe_geo.informe_geo'
#     _description = 'informe_geo.informe_geo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
