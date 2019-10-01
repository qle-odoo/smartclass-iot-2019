install pip3 install camera-discovery

patch line 32
If your are smart use patch system on IOT build

32            if '.' in ip_scope:



    def cameraIP_loop(self):
        camera_devices = {}
        cameras = CameraDiscovery.ws_discovery()
        for camera in cameras:
            devices[camera]['identifier'] = camera
            iot_device = IoTDevice(devices[camera], 'video')
            camera_devices[camera] = iot_device
        return camera_devices
