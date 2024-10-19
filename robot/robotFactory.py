#leave this bit
#seriously mess around with any of it and you program will not work
import robot
import motor
import reedSwitch
import wheel
import threading

class robotFactory:
    robotWidth=16
    wheelRadius=1.55
    
    leftReedPin=14
    rightReedPin=21
    
    leftMotorForwardPin=8
    leftMotorBackwardsPin=25
    
    rightMotorForwardsPin=23
    rightMotorBackwardsPin=24

    def getMotorSpeed(self,speedDataFileName):
        leftMotorSpeed=2.3
        rightMotorSpeed=2.38
        try:
            f=open(speedDataFileName,"r")
            speedData=f.readline()
            f.close()
            speedData=speedData.split(" ")
            leftMotorSpeed=float(speedData[0])
            rightMotorSpeed=float(speedData[-1])
            print("worked")
        except:
            pass
        return leftMotorSpeed,rightMotorSpeed
        
    def makeRobot(self,speedDataFileName):
        GPIOPinlock=threading.Lock()
        leftReedSwitch=reedSwitch.reedSwitch(self.leftReedPin)
        rightReedSwitch=reedSwitch.reedSwitch(self.rightReedPin)

        leftMotor=motor.motor(self.leftMotorForwardPin,self.leftMotorBackwardsPin)
        rightMotor=motor.motor(self.rightMotorForwardsPin,self.rightMotorBackwardsPin)
        
        leftMotorSpeed,rightMotorSpeed=self.getMotorSpeed(speedDataFileName)


        leftWheel=wheel.wheel(leftReedSwitch,leftMotor,leftMotorSpeed,self.wheelRadius,GPIOPinlock)
        rightWheel=wheel.wheel(rightReedSwitch,rightMotor,rightMotorSpeed,self.wheelRadius,GPIOPinlock)
        return robot.robot(leftWheel,rightWheel,self.robotWidth)
        



