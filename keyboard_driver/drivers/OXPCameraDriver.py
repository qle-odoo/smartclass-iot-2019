import base64
import tempfile
import subprocess
from camera_discovery import CameraDiscovery
import cv2

from odoo.addons.hw_drivers.controllers.driver import Driver, event_manager

class OXPCameraDriver(Driver):
    connection_type = 'cameraIP'

    def __init__(self):
        super(OXPCameraDriver, self).__init__(device)
        self._device_type = 'camera'
        self._device_connection = 'network'
        self._device_name = self.dev.card.decode("utf-8")

    @classmethod
    def supported(cls, device):
        return true

    @property
    def device_identifier(self):
        return self.dev['identifier']

    def action(self, data):
        try:
            """
            Take picture and save it to a tmp file.
            Convert this picture in base 64.
            Release Event with picture in data.
            """

            cap = cv2.VideoCapture('restp://' + self.device_identifier + '554/11')
            if cap.isOpened():
                _, frame = cap.read()
                cap.release()
                if _ and frame is not None:
                    retval, b64buffer = cv2.imencode('.jpeg', image)
                    self.data['image'] = base64.b64encode(b64buffer)
                    self.data['message'] = 'Image Captured'
        except subprocess.CalledProcessError as e:
            self.data['message'] = e.output

        event_manager.device_changed(self)
