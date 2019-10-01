# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import cv2

from odoo.addons.hw_drivers.controllers.driver import Driver, event_manager

class OXPCameraIPDriver(Driver):
    connection_type = 'cameraIP'

    def __init__(self, device):
        super(OXPCameraIPDriver, self).__init__(device)
        self._device_type = 'camera'
        self._device_connection = 'network'
        self._device_name = 'Camera IP OXP'

    @classmethod
    def supported(cls, device):
        return True

    def action(self, data):
        try:
            # Choose video stream: nmap --script rtsp-url-brute -p 554 [IP]
            cap = cv2.VideoCapture("rtsp://" + self.device_identifier + "554/11")
            if cap.isOpened():
                _, frame = cap.read()
                cap.release()
                if _ and frame is not None:
                    retval, b64buffer = cv2.imencode('.jpg', image)
                    self.data['image'] = base64.b64encode(b64buffer)
                    self.data['message'] = 'Image captured'
        except subprocess.CalledProcessError as e:
            self.data['message'] = e.output
        event_manager.device_changed(self)

    @property
    def device_identifier(self):
        return self.dev['identifier']
