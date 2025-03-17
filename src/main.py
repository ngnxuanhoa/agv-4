from flask import Flask, render_template, Response, jsonify, request
import os
import cv2
import numpy as np
import threading
import RPi.GPIO as GPIO
from camera import Camera
from motor_controller import MotorController
from navigation import Navigator
from obstacle_detection import ObstacleDetector

# Adjusted template folder path
app = Flask(__name__, template_folder='src/templates')

# Initialize components
camera = Camera()
motor_controller = MotorController()
navigator = Navigator()
obstacle_detector = ObstacleDetector()

# Global variables
autonomous_mode = False
current_map = None

@app.route('/')
def index():
    """Render the main control page"""
    return render_template('index.html')

def gen_frames():
    """Generate camera frames with obstacle detection"""
    while True:
        frame = camera.get_frame()
        if obstacle_detector.detect(frame):
            # Draw obstacle warning
            cv2.putText(frame, 'Obstacle Detected!', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Encode frame to jpg
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(gen_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control/<action>', methods=['POST'])
def control(action):
    """Handle manual control commands"""
    if autonomous_mode:
        return jsonify({'status': 'error', 'message': 'Disable autonomous mode first'})
    
    if action == 'forward':
        motor_controller.forward()
    elif action == 'backward':
        motor_controller.backward()
    elif action == 'left':
        motor_controller.left()
    elif action == 'right':
        motor_controller.right()
    elif action == 'stop':
        motor_controller.stop()
    
    return jsonify({'status': 'success'})

@app.route('/mode', methods=['POST'])
def set_mode():
    """Toggle between manual and autonomous mode"""
    global autonomous_mode
    mode = request.json.get('mode')
    if mode == 'autonomous':
        autonomous_mode = True
        navigator.start_autonomous_navigation()
    else:
        autonomous_mode = False
        navigator.stop_autonomous_navigation()
    return jsonify({'status': 'success', 'mode': mode})

@app.route('/map/generate', methods=['POST'])
def generate_map():
    """Generate map from camera feed"""
    global current_map
    current_map = navigator.generate_map(camera.get_frame())
    return jsonify({'status': 'success'})

@app.route('/map/coordinates', methods=['POST'])
def set_coordinates():
    """Set navigation coordinates"""
    coordinates = request.json.get('coordinates')
    navigator.set_coordinates(coordinates)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    finally:
        # Cleanup
        motor_controller.cleanup()
        GPIO.cleanup()
