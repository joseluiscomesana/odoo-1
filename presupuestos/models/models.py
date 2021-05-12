# -*- coding: utf-8 -*-

from odoo import models, fields, api


class presupuestos(models.Model):
    _name = 'presupuestos.presupuesto'
    _description = 'Presupuesto GeoRedia'

    ensayo = fields.Char(string='Ensayo')
    descripcion = fields.Text(string='Descripción')

