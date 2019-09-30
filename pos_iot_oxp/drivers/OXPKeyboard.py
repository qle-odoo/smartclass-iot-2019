from odoo.addons.hw_drivers.controllers.driver import Driver

class OXPKeyboardDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(OXPKeyboardDriver, self).__init_(device)
        self._device_type = "keyboard"
        self._device_connection = "direct"
        self._device_name = "USB Keyboard"

    @classmethod
    def supported(cls, device):
        for cfg in device:
            for itf in cfg:
                return itf.bInterfaceClass == 3 and itf.bInterfaceProtocol == 1
