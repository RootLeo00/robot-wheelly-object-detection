# Wheelly the Coyote - Object Detection on Raspberry Pi 4B / 3B+
End-to-end object detection using Raspberry Pi 4B / 3B+

##### Table of Contents  
[Install](#install)  
[Usage](#usage)  
[File Details](#file-details)  
[Bill Of Materials](#bill-of-materials)  
[Troubleshooting](#troubleshooting)  


# Install
## Software
1. Clone this repository
```bash
git clone https://github.com/RootLeo00/robot-wheelly-object-detection.git
```
2. Download requirements
```bash
cd robot-wheelly-object-detection
chmod +x setup.sh
./setup.sh
```

# Usage 
3. Start pigpiod daemon
```bash
sudo pigpiod
```
4. Start detection
```bash
python detect.py
```

# File details
```
├──  test  
│    └── testservo.py  - a test to understand if servo is working
│    └── testsonar.py  - a test to understand if sonar is working
│    └── testwheels.py  - a test to understand if motors, wheels and h-bridge are working
|
|
├──  detect.py - file with main that runs the program  
├──  efficientdet_lite0.tflite - pretrained model using EfficientDet0 neural network
├──  efficientdet_lite0_edgetpu.tflite - pretrained model using EfficientDet0 neural network to use with EdgeTPU
├──  requirements.txt  - file with the names of the python modules to download
├──  servo.py - class with Servo functions
├──  setup.sh - file to run to download tflite models and requirements
├──  sonar.py - class with Sonar functions
├──  utils.py - utilities, such as function visualize
├──  wheels.py - class with functions to control motors and wheels
```

# Bill Of Materials
- Raspberry PI 4B
- 2 Trolley Chassis
- 4 Micro DC Motor (Geared) - 90 RPM (6-12V)
- 4 wheels
- L298N Dual H-Bridge Motor Controller
- Ultrasonic Sensor - HC-SR04 (Sonar)
- Jumper wires MM / FM / FF
- USB-C wire
- Cooling Fan
- Power Bank 5200mAh
- 4 batteries AA (1.5 V)
- Raspberry Pi Camera Module 1.3
- Micro Servo 9G 

# Troubleshooting
1. Camera not found
- Make sure that you have enabled camera interface on Raspberry Pi, through command:
```bash
sudo raspi-config
```
- Make sure your system is detecting camera. Try running:
  ```bash 
  vcgencmd get_camera
  ```
  You should get back ```supported=1  detected=1```, indicating that the camera is detected and supported by the operating system. If you get ```detected=0```, then the camera is not being seen by the operating system.
  You can try to force OS to auto detect camera by modyfing boot configuration:
  ```vim 
  sudo vim /boot/config.txt
  ```
  Write somewhere on file:
  ```vim
  camera_auto_detect=1
  ```
  Restart system
  ```bash
  reboot
  ```  
- detect.py use deafult video device on ```/dev/video0```, if you want to change to another (e.g. ```/dev/video1```), you have to launch the program passing the ```--cameraId``` argument. Example:
```bash
python detect.py --cameraId=1
```
2. Raspberry is slow on detect the object

    This is totally normal. If you want to have a faster and more accurate detection, you can use EdgeTPU (e.g. Coral Accelerator) or another type of board

3. Wheels, sonar or servo don't work
   
   Try to run their specific tests. You can find the tests in ```/test``` folder.
