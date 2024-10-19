from motor import motor
from reedSwitch import reedSwitch
import time
import math
import matplotlib.pyplot as plt

#this program is to determine the relationship between throttle and speed


class wheel:
	motor=0
	reedSwitch=0
	def __init__(self,reedSwitch,motor):
		self.motor=motor
		self.reedSwitch=reedSwitch

		
	def setThrottle(self,throttle):
		self.motor.setThrottle(throttle)
		
				
	def driveWheel(self,revolutions,throttle):
		wheelPosition=0
		
		
		
		self.setThrottle(throttle)
		
		while True:
			if wheelPosition>=revolutions:
				self.setThrottle(0)
				break
		
			if self.reedSwitch.pollState():
				wheelPosition+=1
					


		


if __name__=="__main__":
	revolutionsPerTest=10
	numberOfTests=20
	rangeOfTests=1
	minimum=0.1
	throttles=[i*rangeOfTests/(numberOfTests-1)-rangeOfTests/2 for i in range(numberOfTests)]
	throttles=list(filter(lambda x:abs(x)>minimum,throttles))
	print(throttles)
	times=[]
	
	
	
	rightMotor=motor(23,24)
	rightReed=reedSwitch(21)

	leftMotor=motor(8,25)
	leftReed=reedSwitch(14)
	
	#comment one of these lines out depending on which wheel you wish to run
	#wheel=wheel(rightReed,rightMotor)#right wheel
	wheel=wheel(leftReed,leftMotor)#left
	for throttle in throttles:
		start=time.time()
		wheel.driveWheel(revolutionsPerTest,throttle)
		t=time.time()-start
		times.append(t)
		time.sleep(0.5)
		
	plt.scatter(throttles,times)
	plt.title("time vs throttle")
	plt.show()


	speeds=[1/t for t in times]
	plt.scatter(throttles,speeds)
	plt.title("speed vs throttle")
	plt.show()	
	
