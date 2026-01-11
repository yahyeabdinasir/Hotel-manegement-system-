from odoo import models,fields,api

class Rooms(models.Model):
    _name = 'hotel.room'
    _description = 'This is room model'


    name = fields.Char(string='Room Number', readonly=True)
    room_type = fields.Selection([
        ('single','Single'),
        ('couple','Couple')
    ],string='Room Type', required=True)


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hotel.room') or 'new'
        record = super(Rooms, self).create(vals)
        return record