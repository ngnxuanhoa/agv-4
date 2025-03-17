import cv2
import numpy as np

class ObstacleDetector:
    def __init__(self):
        # Parameters for obstacle detection
        self.min_area = 500  # Minimum contour area to be considered an obstacle
        self.threshold = 30  # Threshold for edge detection

    def detect(self, frame):
        """
        Detect obstacles in the frame using computer vision
        Returns True if obstacles are detected, False otherwise
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Detect edges using Canny
        edges = cv2.Canny(blurred, self.threshold, self.threshold * 2)
        
        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, 
                                     cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter contours by area
        obstacles = [cnt for cnt in contours if cv2.contourArea(cnt) > self.min_area]
        
        return len(obstacles) > 0