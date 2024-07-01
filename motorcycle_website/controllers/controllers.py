# -*- coding: utf-8 -*-
# from odoo import http


# class MotorcycleWebsite(http.Controller):
#     @http.route('/motorcycle_website/motorcycle_website', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/motorcycle_website/motorcycle_website/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('motorcycle_website.listing', {
#             'root': '/motorcycle_website/motorcycle_website',
#             'objects': http.request.env['motorcycle_website.motorcycle_website'].search([]),
#         })

#     @http.route('/motorcycle_website/motorcycle_website/objects/<model("motorcycle_website.motorcycle_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('motorcycle_website.object', {
#             'object': obj
#         })
