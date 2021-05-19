from odoo import models, fields, api

class Champs(models.Model):
    _name='presupuestos.solicita'
    _description = 'Solicitud de presupuesto'

    type = fields.Selection([('P','Personalizado'),('R','Prediseñado'),('T','Tutorial')],string="Tipo",required=True)
    customer = fields.Many2one(string="Cliente",comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')

class FieldsModel(models.Model):
    _inherit = 'sale.order'

    @api.onchange('field_many2one')
    def _onchange(self):
        if self.field.many2one.name == '':
            self.field_bool = True
            self.field_char = 'Cambio'

    field_many2one = fields.Many2one('product.template','Campo Many2one')
    field_change = fields.Many2one('product.template', 'Campo Many2one OnChange')
    field_bool = fields.Boolean('Campo Boolean')
    field_char = fields.Char('Campo Char')