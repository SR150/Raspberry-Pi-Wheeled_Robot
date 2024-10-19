# cubsRobot

This is a basic robot I built for cubs to program in python. It uses 2 independently controlled motors for movement. Those motors are controlled using a magnet on each wheel with a reed switch to calibrate motor speed.

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
