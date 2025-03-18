from picamera2 import Picamera2, Preview
import libcamera
import cv2

class Camera:
    def __init__(self):
        self.camera = Picamera2()
        # Configure camera settings
        config = self.camera.create_still_configuration(
            main={"size": (1640, 1232)},
            lores={"size": (640, 480)},
            display="lores"
        )
        self.camera.configure(config)
        # Set white balance mode to off and manually adjust color gains
        self.camera.set_controls({"AwbMode": libcamera.controls.AwbModeEnum.Off})
        self.camera.set_controls({"ColourGains": (2.0, 1.0)})  # Adjust these values to improve color balance
        self.camera.set_controls({"Brightness": 0.5})  # Adjust brightness if necessary
        self.camera.set_controls({"Contrast": 1.0})  # Adjust contrast if necessary
        self.camera.set_controls({"Saturation": 1.0})  # Adjust saturation if necessary
        self.camera.set_controls({"Sharpness": 1.0})  # Adjust sharpness if necessary
        self.camera.start()

    def get_frame(self):
        frame = self.camera.capture_array("main")
        # Convert BGR to RGB if needed
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
