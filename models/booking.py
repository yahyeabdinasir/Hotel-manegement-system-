from odoo import fields, models, api


class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hutel guests'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    number = fields.Char(string="reference number", readonly=True)
    customer_name = fields.Many2one('hotel.customer', tracking=True, string="customer name ")
    guest_room = fields.Many2one("hotel.room", string="room ")
    check_in = fields.Date(string="checkin", default=fields.Date.context_today)
    checkout = fields.Date(string="checkout")
    total_days = fields.Integer(compute="_compute_total_days")

    @api.depends("check_in", 'checkout')
    def _compute_total_days(self):
        for rec in self:
            if rec.check_in and rec.checkout:
                rec.total_days = (rec.checkout - rec.check_in).days
            else:
                rec.total_days=0

    @api.model
    def create(self, vals_list):
        vals_list['number'] = self.env['ir.sequence'].next_by_code('hotel.booking')
        return super(HotelBooking, self).create(vals_list)

    @api.model
    def write(self, vals):
        for rec in self:
            if not rec.number:
                vals['number'] = self.env['ir.sequence'].next_by_code('hotel.booking')

        return super(HotelBooking, self).write(vals)
