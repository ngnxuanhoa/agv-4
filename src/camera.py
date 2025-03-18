from picamera2 import Picamera2, Preview
import libcamera
import cv2
import numpy as np

class Camera:
    def __init__(self):
        self.camera = Picamera2()
        # Configure camera settings
        config = self.camera.create_video_configuration(
            main={"size": (640, 480), "format": "YUV420"},
            lores={"size": (320, 240), "format": "YUV420"},
            display="lores"
        )
        self.camera.configure(config)
        # Set auto white balance
        self.camera.set_controls({"AwbMode": libcamera.controls.AwbModeEnum.Auto})
        # Adjust other settings for better image quality
        self.camera.set_controls({"Brightness": 0.5})
        self.camera.set_controls({"Contrast": 1.0})
        self.camera.set_controls({"Saturation": 1.5})
        self.camera.set_controls({"Sharpness": 1.0})
        # Adjust color gains (experiment with these values)
        self.camera.set_controls({"ColourGains": (1.5, 1.2)})
        self.camera.start()

    def get_frame(self):
        frame = self.camera.capture_array("main")
        # Convert to 3-channel BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_I420)
        # Apply denoising using OpenCV
        frame = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
        # Convert BGR to RGB if needed
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
