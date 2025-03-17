from picamera2 import Picamera2
import cv2
import time

class Camera:
    def __init__(self):
        self.camera = Picamera2()
        
        # Configure camera
        config = self.camera.create_preview_configuration(
            main={"format": 'RGB888',
                  "size": (640, 480)},
            buffer_count=4  # Increase buffer for smooth streaming
        )
        self.camera.configure(config)
        
        # Start camera
        self.camera.start()
        time.sleep(1)  # Wait for camera to initialize

    def get_frame(self):
        """Capture and return a frame from the camera"""
        frame = self.camera.capture_array()
        # Convert RGB to BGR for OpenCV processing
        return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    def release(self):
        """Release camera resources"""
        self.camera.stop()