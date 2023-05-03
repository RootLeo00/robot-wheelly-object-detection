# Wheelly the Coyote - Object Detection on Raspberry Pi 4B / 3B+
End-to-end object detection using Raspberry Pi 4B / 3B+

# Install
1. Clone this repository
```bash
git clone https://github.com/RootLeo00/robot-wheelly-object-detection.git
```
2. Download requirements
```bash
cd robot-wheelly-object-detection
chmod 777 setup.sh
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
1. Raspberry is slow on detect the object

    This is totally normal. If you want to have a faster and more accurate detection, you can use EdgeTPU (e.g. Coral Accelerator) or another type of board

2. wheels, sonar or servo don't work
   try to run their specific tests. You can find the tests in ```/test``` folder.