# -*- coding: utf-8 -*-

from odoo import models, fields, api


class om_hutel(models.Model):
    _name = 'hotel.customer'
    _description = 'htel property '

    name = fields.Char(string="name")
    code = fields.Char(string="code ")
    active=   fields.Boolean(default=False, string="active")
    # company_id: Many2one('res.company')
    # currency_id: Many2one('res.currency')
    # address_id: Many2one('res.partner')
    # floor_ids: One2many('hotel.floor', 'property_id')
    # room_ids: One2many('hotel.room', 'property_id')


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

