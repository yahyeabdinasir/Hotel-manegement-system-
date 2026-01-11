from odoo import models,fields,api

class Rooms(models.Model):
    _name = 'hotel.room'
    _description = 'This is room model'


    name = fields.Char(string='Rooms',required=True)
    room_type = fields.Selection([
        ('single','Single'),
        ('couple','Couple')
    ],string='Room Type', required=True)