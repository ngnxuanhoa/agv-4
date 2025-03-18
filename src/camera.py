from picamera2 import Picamera2, Preview
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
        # Set Auto White Balance
        self.camera.set_controls({"AwbMode": "auto"})
        self.camera.start()

    def get_frame(self):
        frame = self.camera.capture_array("main")
        # Convert BGR to RGB if needed
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
