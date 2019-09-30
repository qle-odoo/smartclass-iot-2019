
from odoo import fields, models

class PoSConfig(models.Model):
    _inherit = 'pos.config'

    iot_keyboard_id = fields.Many2one(
        'iot.device',
        string='Keyboard',
        domain=[('type', '=', 'keyboard')]
    )
