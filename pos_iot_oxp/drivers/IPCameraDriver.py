
import evdev
import os
import time
import fswebcam
from odoo.addons.hw_drivers.controllers.driver import Driver, event_manager

class IPCameraDriver(Driver):
    connection_type = 'usb'

    def __init__(self, device):
        super(IPCameraDriver, self).__init__(device)
        self._device_type = "camera"
        self._device_connection = "network"
        self._device_name = self.dev['device-make-and-model']
        # self._input_device = self._get_evdev_device()

    @classmethod
    def supported(cls, device):
        return True
        # for cfg in device:
        #     for itf in cfg:
        #         return itf.bInterfaceClass == 3 and itf.bInterfaceProtocol == 1

    @classmethod
    def get_device_model(cls, device):
        device_model = ""
        if device.get('device-id'):
            for device_id in [device_lo for device_lo in device['device-id'].split(';')]:
                if any(x in device_id for x in ['MDL', 'MODEL']):
                    device_model = device_id.split(':')[1]
                    break
        elif device.get('device-make-and-model'):
            device_model = device['device-make-and-model']
        return re.sub("[\(].*?[\)]", "", device_model).strip()
        
    # def _get_evdev_device(self):
    #     for path in reversed(evdev.list_devices()):
    #         device = evdev.InputDevice(path)
    #         if self.dev.idVendor == device.info.vendor and self.dev.idProduct == device.info.product:
    #             return device

    # def run(self):
    #     for event in self._input_device.read_loop():
    #         if event.type == evdev.ecodes.EV_KEY:
    #             data = evdev.categorize(event)
    #             if data.keystate:
    #                 self.data['value'] = data.keycode.replace('KEY_', '')
    #                 event_manager.device_changed(self)

    def action(self, data):
        if data.get('action') == 'change_led':
            self._change_led_status()

            os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --save /home/pi/to_transmit/%H%M%S.jpg')
            time.sleep(15)

    # def _change_led_status(self):
    #     led_status = 0 in self._input_device.leds()
    #     self._input_device.set_led(0, int(not led_status))
