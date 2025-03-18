# AGV Control System

An autonomous guided vehicle (AGV) control system using Raspberry Pi 4 with web-based monitoring and control capabilities.

## Hardware Requirements

- Raspberry Pi 4 2GB or higher
- Raspberry Pi Camera Module 2 NoIR (v2.1 or newer)
- L298N Motor Driver
- 4x DC Motors (12V)
- 12V Power Supply
- Motor wheels and chassis
- Jumper wires
- Breadboard

## Software Requirements

- Raspberry Pi OS Lite (Bookworm)
- Python 3.11 or higher
- OpenCV
- Flask
- NumPy
- RPi.GPIO
- picamera2 (for Raspberry Pi Camera)
- libcamera (Camera system)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ngnxuanhoa/agv-4.git
cd agv-4
```

2. Install Camera Libraries and Dependencies:
```bash
# Update system packages
sudo apt update
sudo apt upgrade -y

# Install camera libraries and dependencies
sudo apt install -y python3-picamera2
sudo apt install -y python3-libcamera
sudo apt install -y python3-opencv
sudo apt install -y libcamera-tools
sudo apt install -y libcamera-apps

# Test camera installation
libcamera-hello   # Should show camera preview
libcamera-jpeg -o test.jpg  # Should capture a test image
```

3. Install other required packages:
```bash
# Install Python and required system packages
sudo apt install -y python3-pip python3-rpi.gpio

# Install Python dependencies
python3 -m pip install -r requirements.txt
```

4. Enable and Configure Camera:
```bash
# Edit /boot/config.txt to enable camera
sudo nano /boot/config.txt

# Add or uncomment these lines:
camera_auto_detect=1
dtoverlay=camera

# Save and reboot
sudo reboot

# After reboot, verify camera setup
v4l2-ctl --list-devices    # Should list your camera device

# Set camera permissions (if needed)
sudo usermod -a -G video $USER

# Test camera
libcamera-hello   # Should show camera preview
libcamera-jpeg -o test.jpg  # Capture test image
```

5. Create required directories:
```bash
# Create static and templates directories
mkdir -p ~/agv-4/src/static
mkdir -p ~/agv-4/src/templates
```

6. Configure GPIO pins:
```python
# Check src/motor_controller.py for pin configuration
# Default GPIO pin setup:
# Motor A (Left):
#   - IN1: GPIO 17
#   - IN2: GPIO 27
#   - ENA: GPIO 22
# Motor B (Right):
#   - IN3: GPIO 23
#   - IN4: GPIO 24
#   - ENB: GPIO 25
```

## Camera Configuration

1. Basic Camera Settings:
```python
# in src/camera.py
from picamera2 import Picamera2

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
        self.camera.start()
```

2. Camera Troubleshooting:
```bash
# Check camera module is recognized
ls -l /dev/video*

# Test camera with different applications
libcamera-hello     # Preview
libcamera-jpeg -o test.jpg    # Still capture
libcamera-vid -t 10000 -o test.h264    # Video capture

# Check camera logs
dmesg | grep -i camera

# Verify permissions
groups ${USER}    # Should include 'video' group
```

## Requirements.txt
```txt
flask>=3.0.0
opencv-python>=4.8.0
numpy>=1.24.0
RPi.GPIO>=0.7.0
picamera2>=0.3.12
```

[... rest of the README content ...]

## Troubleshooting

[... previous troubleshooting content ...]

4. Camera Issues:
   - No camera detected:
     ```bash
     # Check camera connection
     vcgencmd get_camera
     
     # Check if camera interface is enabled
     sudo raspi-config
     
     # Verify camera module
     ls -l /dev/video*
     ```
   
   - Camera permission issues:
     ```bash
     # Add user to video group
     sudo usermod -a -G video $USER
     
     # Verify groups
     groups ${USER}
     ```
   
   - Poor image quality:
     ```bash
     # Test with different resolutions
     libcamera-jpeg -o test_hq.jpg --width 2028 --height 1520
     
     # Check camera focus
     # Manually adjust camera focus if using adjustable lens
     ```

   - Camera errors in code:
     ```python
     # Debug camera initialization
     from picamera2 import Picamera2
     picam2 = Picamera2()
     print(picam2.camera_properties)  # Check camera properties
     ```

[... rest of the README content ...]
