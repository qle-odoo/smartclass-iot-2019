# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import tempfile
import subprocess
import requests
import base64

from odoo.addons.hw_drivers.controllers.driver import event_manager, Driver


class IPCamDriver(Driver):
    connection_type = 'cameraIP'

    def __init__(self, device):
        super(IPCamDriver, self).__init__(device)
        self._device_type = 'camera'
        self._device_connection = 'network'
        self._device_name = "IPCAM"
        self._device_identifier = "IPCAMERA"

    @classmethod
    def supported(cls, device):
        return True

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

            session = requests.Session()
            session.auth = ('admin', 'admin')
            content = session.get('http://192.168.2.27/auto.jpg').content
            encodedBytes = base64.b64encode(content)
            self.data['image'] = encodedBytes
            self.data['message'] = 'Image captured'
        except subprocess.CalledProcessError as e:
            self.data['message'] = e.output

        event_manager.device_changed(self)