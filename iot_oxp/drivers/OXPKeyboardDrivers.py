# -*- coding: utf-8 -*-

import pprint

from odoo.addons.hw_drivers.controllers.driver import Driver, event_manager


pp = pprint.PrettyPrinter(indent=4)


class OXPKeyboardDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(OXPKeyboardDriver, self).__init__(device)
        self._device_type = 'keyboard'
        self._device_connection = 'direct' #(network or direct here ) changes the device icon show in IOT module. (direct when corrected to IOT, and network when on LAN device)
        self._device_name = 'USB Keyboard'

    @classmethod
    def supported(cls, device):
        '''
        Method to Check if device is supported or not 
        device will be have list of devices using python lisb
        i.e. USb loop gives all USB connected 

        return bool: if supported True else False
        '''
        pp.pprint(device)
        for cfg in device:
            for itf in cfg:
