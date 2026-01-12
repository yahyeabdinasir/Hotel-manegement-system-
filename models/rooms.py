from odoo import models, fields, api


class Rooms(models.Model):
    _name = 'hotel.room'
    _description = 'This is room model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    Number = fields.Char(string='Room Id', readonly=True)

    room_type = fields.Selection([
        ('single', 'Single'),
        ('couple', 'Couple'),
        ('Suite', 'Suite'),
    ], string='Room Type', required=True)

    price_night = fields.Float(string="price night")

    Floor_Number = fields.Char(string="Floor NO")

    Number_bed = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ], steing="Bed No", required=True)

    Room_Description = fields.Char(string="description")

    @api.model
    def create(self, vals):
        vals['Number'] = self.env['ir.sequence'].next_by_code('hotel.room') or 'new'
        record = super(Rooms, self).create(vals)
        return record

    @api.model
    def write(self, vals):
        for rec in self:
            if not rec.Number:
                vals['Number'] = self.env['ir.sequence'].next_by_code('hotel.room')
        record = super(Rooms, self).write(vals)

        return record

    @api.onchange("room_type", "Number_bed")
    def _onchange_room_price(self):
        for record in self:
            if record.room_type == 'single':
                if record.room_type == 'single' and record.Number_bed == '1':
                    record.price_night = 40
                else:
                    record.price_night = 50

            elif record.room_type == 'couple':
                if record.room_type == 'couple' and record.Number_bed == '2' or record.Number_bed == '3':
                    record.price_night = 80

                else:
                    record.price_night = 60
            elif record.room_type == 'Suite':
                if record.room_type == 'Suite' and record.Number_bed == '2' or record.Number_bed == '3':
                    record.price_night = 130
                else:
                    record.price_night = 100



