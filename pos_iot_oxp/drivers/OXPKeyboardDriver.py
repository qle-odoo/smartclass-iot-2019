# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from usb import util

from odoo.addons.hw_drivers.controllers.driver import Driver

class OXPKeyboardDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(OXPKeyboardDriver, self).__init__(device)
        self._device_type = 'keyboard'
        self._device_connection = 'direct'
        self._device_name = self._get_keyboard_name()

    @classmethod
    def supported(cls, device):
        for cfg in device:
            for itf in cfg:
                if itf.bInterfaceClass == 3 and itf.bInterfaceProtocol == 1:
                    return True
        return False

    def _get_keyboard_name(self):
        try:
            manufacturer = util.get_string(self.dev, 256, self.dev.iManufacturer)
            product = util.get_string(self.dev, 256, self.dev.iProduct)
            return "%s - %s" % (manufacturer, product)
        except ValueError as e:
            return "Unknown keyboard"
