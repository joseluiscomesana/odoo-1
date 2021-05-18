from odoo import models, fields, api

class Champs(models.Model):
    _name='presupuestos.solicita'
    _description = 'Solicitud de presupuesto'

    type = fields.Selection([('P','Personalizado'),('R','Prediseñado'),('T','Tutorial')],string="Tipo",required=True)
    customer = fields.Many2one(String="Cliente",comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
