# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import evdev

from usb import util

from odoo.addons.hw_drivers.controllers.driver import Driver, event_manager

class OXPKeyboardDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(OXPKeyboardDriver, self).__init__(device)
        self._device_type = 'keyboard'
        self._device_connection = 'direct'
        self._device_name = self._get_keyboard_name()
        self._input_device = self._get_evdev_device()

    @classmethod
    def supported(cls, device):
        for cfg in device:
            for itf in cfg:
                if itf.bInterfaceClass == 3 and itf.bInterfaceProtocol == 1:
                    return True
        return False


    def _get_evdev_device(self):
        for path in reversed(evdev.list_devices()):
            device = evdev.InputDevice(path)
            if self.dev.idVendor == device.info.vendor and self.dev.idProduct == device.info.product:
                return device

    def run(self):
        for event in self._input_device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                data = evdev.categorize(event)
                if data.keystate:
                    self.data['value'] = data.keycode.replace('KEY_', '')
                    event_manager.device_changed(self)
                    

    def action(self, data):
        if data.get('action') == 'change_led':
            self._change_led_status()
        elif data.get('action') == 'change_led_multiple':
            self._change_led_multiple()
            
    def _change_led_status(self):
        led_status = 0 in self._input_device.leds()
        self._input_device.set_led(0, int(not led_status))
    
    def _change_led_multiple(self):

        self._input_device.set_led(0, 1)
        self._input_device.set_led(1, 1)
        self._input_device.set_led(2, 1)
        sleep(1)
        
        self._input_device.set_led(0, 0)
        self._input_device.set_led(1, 0)
        self._input_device.set_led(2, 0)

    def _get_keyboard_name(self):
        try:
            manufacturer = util.get_string(self.dev, 256, self.dev.iManufacturer)
            product = util.get_string(self.dev, 256, self.dev.iProduct)
            return "%s - %s" % (manufacturer, product)
        except ValueError as e:
            return "Unknown keyboard"