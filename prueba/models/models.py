# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name = 'prueba.visit'
    _description = 'Visit'
    _inherit = "res.partner"

    name = fields.Char(string='Descripción')
    customer = fields.Char(string='Cliente')
  #  customer = fields.Many2one(context='Cliente', comodel_name="res.partner")
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P','Presencial'),('W','Whatsapp'),('T','Telefónica')],string='Tipo',required=True)
    done = fields.Boolean(string='Realizada')
    image = fields.Binary(string="Imagen")

    def toggle_state(self):
        self.done = not self.done
