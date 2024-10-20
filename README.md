# cubsRobot

This is a basic robot I built for cubs to program in python. It uses 2 independently controlled motors for movement. Those motors are controlled using a magnet on each wheel with a reed switch to calibrate motor speed. This allows the use of DCC stepper motors.

see hardware file for construction details.

## Interface
get a robot object from the robotFactory object.

### Movement commands
Note: distance is in cm

robot.forwards(distance)

robot.backwards(distance)


### Turning Commands
angle is in degrees. It is an optional argument, which if not provided defaults to 90.

robot.turnLeft(angle)

robot.turnRight(angle) 

button.py is a simple program to run main.py when a button is pressed. I set it up to run on startup. The cubs then wrote the program on a usb stick which was plugged into the raspberry pi.

an example program is in robot/main.py




## Hardware
to build the robot you will need:

1 raspberry pi

2 motors

motor controler for 2 motors

2 magnets

2 wheels

2 reed switch

1 resistor
battery for raspberry pi and motor
wood or plastic to mount all components.

## Instalation
Download the code and run. Main.py has an example program you can run.

### Running programs off a USB stick
Place the contents of Robot on the USB stick.

Determine the path to the usb stick by navigating to the USB stick via command line.

Copy the path to the USB stick into the variable path in button.py

(Optional) Set button.py to run on startup by running the command sudo nano /etc/rc.local then adding

sudo python3 (path to button.py)&

to the file.

