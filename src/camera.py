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
        # Set Auto White Balance using the correct control value
        self.camera.set_controls({"AwbMode": libcamera.controls.AwbModeEnum.Auto})
        # Adjust color gains to balance colors (tweak these values)
        self.camera.set_controls({"ColourGains": (1.2, 1.2)})  # Adjust to remove yellow tint
        self.camera.set_controls({"Brightness": 0.5})  # Adjust brightness if necessary
        self.camera.set_controls({"Contrast": 1.0})  # Adjust contrast if necessary
        self.camera.set_controls({"Saturation": 1.0})  # Adjust saturation if necessary
        self.camera.start()

    def get_frame(self):
        frame = self.camera.capture_array("main")
        # Convert BGR to RGB if needed
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
