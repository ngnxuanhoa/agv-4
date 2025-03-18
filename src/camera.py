from picamera2 import Picamera2, Preview
import libcamera
import cv2

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
        # Apply denoising
        self.apply_denoising()
        self.camera.start()

    def apply_denoising(self):
        # Denoising using OpenCV
        frame = self.camera.capture_array("main")
        frame = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
        return frame

    def get_frame(self):
        frame = self.apply_denoising()
        # Convert BGR to RGB if needed
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
