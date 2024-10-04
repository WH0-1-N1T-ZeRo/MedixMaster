# -*- coding: utf-8 -*-
# from odoo import http


# class MedixMaster(http.Controller):
#     @http.route('/medix_master/medix_master', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medix_master/medix_master/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('medix_master.listing', {
#             'root': '/medix_master/medix_master',
#             'objects': http.request.env['medix_master.medix_master'].search([]),
#         })

#     @http.route('/medix_master/medix_master/objects/<model("medix_master.medix_master"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medix_master.object', {
#             'object': obj
#         })

