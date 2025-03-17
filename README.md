# AGV Control System

An autonomous guided vehicle (AGV) control system using Raspberry Pi 4 with web-based monitoring and control capabilities.

## Hardware Requirements

- Raspberry Pi 4 2GB
- Raspberry Pi Camera Module 2 NoIR
- L298N Motor Driver
- DC Motors
- Power Supply

## Software Requirements

- Raspberry Pi OS Lite (Bookworm)
- Python 3.x
- OpenCV
- Flask
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ngnxuanhoa/agv-4.git
cd agv-4
```

2. Install required packages:
```bash
sudo apt update
sudo apt install -y python3-pip python3-opencv
pip3 install -r requirements.txt
```

3. Enable camera interface:
```bash
sudo raspi-config
# Navigate to Interface Options -> Camera -> Enable
```

## Usage

1. Start the AGV control server:
```bash
python3 src/main.py
```

2. Access the web interface:
Open a web browser and navigate to `http://<raspberry-pi-ip>:5000`

## Features

- Live camera streaming via web browser
- Automatic map generation from camera feed
- Obstacle detection using computer vision
- Autonomous navigation based on map coordinates
- Manual control through web interface (forward, backward, left, right, stop)