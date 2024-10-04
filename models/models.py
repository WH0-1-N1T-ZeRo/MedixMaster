# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class medix_master(models.Model):
#     _name = 'medix_master.medix_master'
#     _description = 'medix_master.medix_master'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

