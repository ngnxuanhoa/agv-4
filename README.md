# AGV Control System

An autonomous guided vehicle (AGV) control system using Raspberry Pi 4 with web-based monitoring and control capabilities.

## Hardware Requirements

- Raspberry Pi 4 2GB or higher
- Raspberry Pi Camera Module 2 NoIR (v2.1 or newer)
- L298N Motor Driver Module
- 4x DC Motors (12V)
- 12V/2A Power Supply
- Motor wheels and chassis
- Jumper wires
- Breadboard
- Power bank for Raspberry Pi (recommended)

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
```

3. Enable and Configure Camera:
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

# Set camera permissions
sudo usermod -a -G video $USER

# Test camera
libcamera-hello   # Should show camera preview
libcamera-jpeg -o test.jpg  # Capture test image
```

4. Install other required packages:
```bash
# Install Python and required system packages
sudo apt install -y python3-pip python3-rpi.gpio

# Install Python dependencies from requirements.txt
python3 -m pip install -r requirements.txt
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

## Requirements.txt
```txt
flask>=3.0.0
opencv-python>=4.8.0
numpy>=1.24.0
RPi.GPIO>=0.7.0
picamera2>=0.3.12
```

## Project Structure
```
agv-4/
├── src/
│   ├── camera.py           # Camera interface and video streaming
│   ├── main.py            # Main Flask application
│   ├── motor_controller.py # Motor control interface
│   ├── navigation.py      # Navigation and path planning
│   ├── obstacle_detection.py # Obstacle detection logic
│   ├── static/           # Static files (generated maps, etc.)
│   └── templates/        # HTML templates
│       └── index.html    # Web interface template
├── requirements.txt      # Python package dependencies
└── README.md            # Project documentation
```

## Development Setup

1. Set up Python virtual environment (recommended):
```bash
# Install venv module
sudo apt install python3-venv

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

2. Enable debug mode for development:
```bash
export FLASK_DEBUG=1
python3 src/main.py
```

## Usage

1. Start the AGV control server:
```bash
# Navigate to project directory
cd ~/agv-4

# If using virtual environment
source venv/bin/activate

# Start the application
python3 src/main.py
```

2. Access the web interface:
- Open a web browser and navigate to `http://<raspberry-pi-ip>:5000`
- Default port is 5000
- Make sure your device is on the same network as the Raspberry Pi

## Features

- Live camera streaming via web browser
- Real-time obstacle detection using computer vision
- Automatic map generation from camera feed
- Autonomous navigation capabilities
- Manual control through web interface:
  - Forward/Backward movement
  - Left/Right turning
  - Emergency stop
  - Mode switching (Manual/Autonomous)

## Troubleshooting

1. Camera Issues:
   ```bash
   # Check if camera is detected
   v4l2-ctl --list-devices
   
   # Verify camera device
   ls -l /dev/video*
   
   # Check camera permissions
   groups ${USER}    # Should include 'video' group
   
   # Test camera functionality
   libcamera-hello
   libcamera-jpeg -o test.jpg
   ```

2. Motors not responding:
   ```bash
   # Check GPIO permissions
   ls -l /dev/gpiomem    # Should be readable by 'gpio' group
   sudo usermod -a -G gpio $USER
   
   # Test GPIO pins
   gpio readall    # Check pin states
   ```

3. Web interface not accessible:
   ```bash
   # Check network connectivity
   hostname -I    # Get Raspberry Pi IP address
   
   # Test Flask server
   curl http://localhost:5000
   
   # Check firewall settings
   sudo ufw status
   ```

## Network Configuration:
```bash
# Configure WiFi
sudo raspi-config
# System Options -> Wireless LAN
# Enter your WiFi SSID and password

# Find Raspberry Pi's IP address
hostname -I
# or
ip addr show
```

## Maintenance

1. Regular Checks:
   - Camera lens cleaning
   - Motor alignment
   - Wheel condition
   - Battery levels
   - Cable connections

2. Software Updates:
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Update Python packages
   pip install --upgrade -r requirements.txt
   ```

3. Backup:
   ```bash
   # Backup configuration
   cp -r ~/agv-4 ~/agv-4-backup-$(date +%Y%m%d)
   ```

## Safety Considerations

1. Physical Safety:
   - Ensure clear operating space
   - Keep cables properly managed
   - Install emergency stop button
   - Test in controlled environment first

2. System Safety:
   - Set motor speed limits
   - Implement collision detection
   - Regular calibration of sensors
   - Backup power management

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Last Updated
2025-03-18 by @ngnxuanhoa ▋
