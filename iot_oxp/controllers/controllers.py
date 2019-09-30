# -*- coding: utf-8 -*-
from odoo import http

# class IotOxp(http.Controller):
#     @http.route('/iot_oxp/iot_oxp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iot_oxp/iot_oxp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iot_oxp.listing', {
#             'root': '/iot_oxp/iot_oxp',
#             'objects': http.request.env['iot_oxp.iot_oxp'].search([]),
#         })

#     @http.route('/iot_oxp/iot_oxp/objects/<model("iot_oxp.iot_oxp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iot_oxp.object', {
#             'object': obj
#         })