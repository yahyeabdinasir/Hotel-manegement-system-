

from odoo import models, fields, api


class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'hotel property'
    _inherit = ['mail.thread' , 'mail.activity.mixin']


    number=fields.Char(string="number")

    Full_name = fields.Char(string="name")
    is_guest = fields.Boolean(string="is guest")
    title = fields.Selection([
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms'),
        ('dr', 'Dr'),
    ])
    image = fields.Image(string="image")

    guest_type = fields.Selection([
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
        ('agent', 'Travel Agent'),
    ])

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    preferred_language = fields.Many2one('res.lang')
    nationality = fields.Char(string="nationality ")

    email = fields.Char(string="email")
    phone = fields.Char(string="phone")
    country_id = fields.Many2one('res.country', string="Country ")

    @api.model
    def create(self, vals_list):
        vals_list["number"] = self.env["ir.sequence"].next_by_code('hotel.customer')
        return super(HotelCustomer, self).create(vals_list)


    def write(self, vals):
        for rec in self:
            if  not rec.guest_number:
                vals["number"] = self.env["ir.sequence"].next_by_code('hotel.customer')
        return super(HotelCustomer, self).write(vars())
