
## HOSAFE Megapixel IP Camera
## H2MD6PA  admin admin

#import rtsp
#client = rtsp.Client(rtsp_server_uri = 'rtsp://192.168.2.27:554/mpeg4')
#client.read().show()
#client.close()


#http://192.168.2.27/tmpfs/auto.jpg?1569926397243


#def downloadimg(self):
#        import datetime
#        imgurl = self.getdailyimg();
##        imgfilename = datetime.datetime.today().strftime('%Y%m%d') + '_' + imgurl.split('/')[-1]
#        with open(IMGFOLDER + imgfilename, 'wb') as f:
#            f.write(self.readimg(imgurl))
#        self.LASTIMG = IMGFOLDER + imgfilename


#import requests

#session = requests.Session()
##session.auth = ('admin', 'admin')

#with open('IPCAM_1490534565948.jpg', 'wb') as f:
 #   f.write(session.get('http://192.168.2.27/tmpfs/auto.jpg?1569926397243').content)


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
        self._device_name = "HOSAFE"
        self._device_identifier = "H2MD6PA"

    @classmethod
    def supported(cls, device):
        return True

    def action(self, data):
        try:
            """
            Take picture and save it to a tmp file.
            Convert this picture in base 64.
            Release Event with picture in data.
            """

            session = requests.Session()
            session.auth = ('admin', 'admin')
            content = session.get('http://192.168.2.27/tmpfs/auto.jpg?1569926397243').content
            encodedBytes = base64.b64encode(content)
            self.data['image'] = encodedBytes
            self.data['message'] = 'Image captured'
        except subprocess.CalledProcessError as e:
            self.data['message'] = e.output

        event_manager.device_changed(self)