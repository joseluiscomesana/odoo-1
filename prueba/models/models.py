# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class Visit(models.Model):
    _name = 'prueba.visit'
    _description = 'Visitación'
 
    name = fields.Char(string='Descripción')
    # customer = fields.Char(string='Cliente')
    # customer = fields.Many2one(context='Cliente', comodel_name="res.partner")
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P','Presencial'),('W','Whatsapp'),('T','Telefónica')],string='Tipo',required=True)
    done = fields.Boolean(string='Realizada')
    image = fields.Binary(string="Imagen")

    def cambiar_hecho(self):
        self.done = not self.done

   #ORM 
    def f_create(self):
        visit ={
            'name':'ORM test',
            'customer':4,
            'date':str(datetime.date(2020,8,6)),
            'type':'P',
            'done':False
        }
        print(visit)
        self.env['prueba.visit'].create(visit)
    
    def f_search_update(self):
        print(len(self)," registros encontrados.")
        for a in self:
            print("a:",a.name)
            visit = self.env['prueba.visit'].browse([a.id])
            a.write({'name':'ORM test write'})

    def f_delete(self):
        visit = self.env['prueba.visit'].browse(1)
        visit.unlink()


class VisitReport(models.AbstractModel):
    
    _name='report.prueba.report_visit_card'
    _description = 'Informe tipo tarjeta'

    @api.model
    def _get_report_values(self,docids,data=None):
        # report_obj = self.env['ir.actions.report']
        # report = report_obj._get_report_from_name('prueba.report_visit_card')
        return{
           'doc_ids':docids,
           'doc_model':self.env['prueba.visit'],
           'docs':self.env['prueba.visit'].browse(docids)
        }

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    advertencia = fields.Char(string='Advertencia')
    zone = fields.Selection([('N', 'Norte'), ('C', 'Centro'), ('S', 'Sur')],string='Zona comercial')