# -*- coding: utf-8 -*-

from odoo import models, fields, api

class POSConfig(models.Model):
    _inherit = 'pos.config'

    iface_keyboard_id = fields.Many2one('iot.device',
                        domain="[('type', '=', 'keyboard'),\
                                '|', ('company_id', '=', False),\
                                ('company_id', '=', company_id)]")