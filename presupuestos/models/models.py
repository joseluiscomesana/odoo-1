# -*- coding: utf-8 -*-

from odoo import models, fields, api


class presupuestos(models.Model):
    _name = 'presupuestos.presupuesto'
    _description = 'Presupuesto GeoRedia'

    ensayo = fields.Char(string='Ensayo')
    descripcion = fields.Text(string='Descripción')
    artic = fields.Many2one(string='Articulo', comodel_name='product.template', ondelete='restrict')

    articName = fields.Char('Nombre',related='artic.name',readonly=False)

class articuloExtend(models.Model):
    _name = 'presupuestos.articulos'
    _description = 'Artículos'
    _inherit = 'product.template'

    def name_get(self):
        result =[]
        for art in self:
            name = '%s (%s)' % (art.id,art.name)
            result.append((art.id,name)) 
        return result

