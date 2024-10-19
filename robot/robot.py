import math
import threading

class robot:
	leftWheel=0
	rightWheel=0
	wheelSeperatonDistanceCm=0
	speed=7
	def __init__(self,leftWheel,rightWheel,wheelSeperatonDistanceCm):
					
		self.leftWheel=leftWheel
		self.rightWheel=rightWheel

		self.wheelSeperatonDistanceCm=wheelSeperatonDistanceCm
		
	def runMotors(self,leftDistance,rightDistance):
		leftWheelThread=threading.Thread(target=self.leftWheel.driveWheel, args=(leftDistance,self.speed))
		rightWheelThread=threading.Thread(target=self.rightWheel.driveWheel, args=(rightDistance,self.speed))
		
		leftWheelThread.start()
		rightWheelThread.start()
		
		leftWheelThread.join()
		rightWheelThread.join()


	def forwards(self,distance):
		self.runMotors(distance,distance)
		
		
	def backwards(self,distance):
		self.forwards(self,-distance)
		
		
	def turnLeft(self,angle=90):
		distance=angle/360*math.pi*self.wheelSeperatonDistanceCm*2
		self.runMotors(0,distance)
		
	def turnRight(self,angle=90):
		distance=angle/360*math.pi*self.wheelSeperatonDistanceCm*2
		self.runMotors(distance,0)

	def saveSpeed(self,speedDataFileName):
		f=open(speedDataFileName,"w")
		f.write(str(leftWheel.motorRevolutionsPerSecond)+"  "+str(rightWheel.motorRevolutionsPerSecond))
		f.close()
		
		

