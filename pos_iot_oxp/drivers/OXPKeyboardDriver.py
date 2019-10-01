
import evdev

from odoo.addons.hw_drivers.controllers.driver import Driver, event_manager

class OXPKeyboardDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(OXPKeyboardDriver, self).__init__(device)
        self._device_type = "keyboard"
        self._device_connection = "direct"
        self._device_name = "USB Keyboard"
        self._input_device = self._get_evdev_device()

    @classmethod
    def supported(cls, device):
        for cfg in device:
            for itf in cfg:
                return itf.bInterfaceClass == 3 and itf.bInterfaceProtocol == 1

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
        if data.get('action') == 'change_numlock_led':
            self._change_led_status(0)
        elif data.get('action') == 'change_capslock_led':
            self._change_led_status(1)

    def _change_led_status(self, led_index):
        led_status = led_index in self._input_device.leds()
        self._input_device.set_led(led_index, int(not led_status))

