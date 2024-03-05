# POV-roomba
A web remote controller with video stream for a roomba with a camera on it

## Instructions
install from source bluez 5.66
first run:
sudo apt-get update
sudo apt-get install libdbus-1-dev libudev-dev libical-dev libreadline-dev libglib2.0-dev libdbus-glib-1-dev libusb-dev systemd libsystemd-dev
https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation

execute 
```
sudo modprobe bcm2835-v4l2
```
run runserver.sh on a raspberry pi (tested on raspi 3b)
create a linux service to run this script on boot


### docs
- https://github.com/iRobotEducation/irobot-edu-python-sdk
- https://www.youtube.com/watch?v=5QAHlZoPlgI
- https://www.highvoltagecode.com/post/webrtc-on-raspberry-pi-live-hd-video-and-audio-streaming
- https://github.com/PietroAvolio/uv4l-webrtc-raspberry-pi/tree/master
- https://github.com/t2age/wl-p2p-av?tab=readme-ov-file
