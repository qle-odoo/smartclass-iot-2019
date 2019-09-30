# -*- coding: utf-8 -*-

import pprint
from odoo.addons.hw_drivers.controllers.driver import Driver

pp = pprint.PrettyPrinter(indent=4)


class OXPKeyboardDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(OXPKeyboardDriver, self).__init__(device)
        self._device_type = 'keyboard' 
        self._device_connection = 'direct' # possible value : direct - network - bluetooth - serial - hdmi ; changes the icon in ui, new type need to be handled client side
        self._device_name = 'USB Keyboard'


    @classmethod
    def supported(cls, device):
        for cfg in device:
            for itf in cfg:
                return itf.bInterfaceClass == 3 and itf.bInterfaceProtocol == 1:
        return False