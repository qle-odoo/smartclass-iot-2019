# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    iot_keyboard_id = fields.Many2one('iot.device', domain="[('type', '=', 'keyboard'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
