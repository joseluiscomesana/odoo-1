# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Car(models.Model):
    _name = 'odoo_model_advanced.car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')
    customer = fields.Many2one(comodel_name='res.users',
                               string='Cliente')


class UserExtended(models.Model):

    _inherit = 'res.users'

    def name_get(self):
        result = []
        for user in self:
            name = '%s (%s)' % (user.name, user.phone)
            result.append((user.id, name))
        return result












