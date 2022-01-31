
# NetworkRobot

* User will be able to control the robot over a network connection.
* The robot will stream a video feed to the user.

## Description

This project runs on a host pc and a Raspberry Pi. The host pc receives inputs from a video game controller and sends the axis inputs over a socket to the robot. 
Once the robot receives the inputs, it sends commands to the motors on the chassis. The robot simultaneously sends a video stream to the host pc. 

## Getting Started

### Dependencies

* Windows 10
* Python
* numpy
* pygame
* opencv
* socket
* time
* threading
* picamera
* RPi.GPIO

## Help

If the robot inputs are backwards, just change the sign for the motor values.

## Authors

Tyler Moody 

## Version History

* 0.1
    * Initial Release
