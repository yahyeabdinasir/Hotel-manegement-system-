# -*- coding: utf-8 -*-
# from odoo import http


# class OmHutel(http.Controller):
#     @http.route('/om_hutel/om_hutel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hutel/om_hutel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hutel.listing', {
#             'root': '/om_hutel/om_hutel',
#             'objects': http.request.env['om_hutel.om_hutel'].search([]),
#         })

#     @http.route('/om_hutel/om_hutel/objects/<model("om_hutel.om_hutel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hutel.object', {
#             'object': obj
#         })

