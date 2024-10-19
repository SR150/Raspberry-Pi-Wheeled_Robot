from motor import motor
from reedSwitch import reedSwitch
import time
import math

class wheel:
	motor=0
	reedSwitch=0
	motorRevolutionsPerSecond=3
	speedDataPoints=60
	wheelPosition=0
	circumference=0
	everSeenMagnet=False
	GPIOLock=0
	def __init__(self,reedSwitch,motor,motorRevolutionsPerSecond,radius,GPIOLock):
		self.motor=motor
		self.reedSwitch=reedSwitch
		self.motorRevolutionsPerSecond=motorRevolutionsPerSecond
		self.circumference=radius*2*math.pi
		self.GPIOLock=GPIOLock
		
		
		
	def correctSpeed(self,timeForOneRotation,throttle):
		if throttle<0:
			return
		rotationsPerSecond=1/timeForOneRotation
		rotationsPerSecondAtFullThrottle=abs(rotationsPerSecond/throttle)
		
		self.motorRevolutionsPerSecond=(self.motorRevolutionsPerSecond*self.speedDataPoints+rotationsPerSecondAtFullThrottle)/(self.speedDataPoints+1)
		self.speedDataPoints+=1
		
		
		
	def getThrottle(self,targetRevolutionsPerSecond):
		return targetRevolutionsPerSecond/self.motorRevolutionsPerSecond

		
	def done(self,target,distance):
		if distance>0 and target<=self.wheelPosition:
			return True
		if distance<0 and target>=self.wheelPosition:
			return True
		if distance==0:
			return True
		return False
		
	def setThrottle(self,throttle):
		with self.GPIOLock:
			self.motor.setThrottle(throttle)
		
				
	def driveWheel(self,distance,speed):
		revolutions=distance/self.circumference
		revolutionsPerSecond=speed/self.circumference
		if distance<0:
			revolutionsPerSecond*=-1
		
		
		last=time.time()
		target=self.wheelPosition+revolutions
		seenMagnet=False
		lastSeenMagnet=0
		
		throttle=self.getThrottle(revolutionsPerSecond)
		self.setThrottle(throttle)
		
		while True:
			if self.done(target,distance):
				self.setThrottle(0)
				break
			
			timePassed=time.time()-last
			last=time.time()
			self.wheelPosition=self.wheelPosition+self.motorRevolutionsPerSecond*timePassed*throttle
			
			
			#check if the wheel 0 position is reached and if so correct the position
			if self.reedSwitch.pollState():
				self.wheelPosition=round(self.wheelPosition)
				if seenMagnet:
					revolutionTime=time.time()-lastSeenMagnet
					lastSeenMagnet=time.time()
					self.correctSpeed(revolutionTime,throttle)
					throttle=self.getThrottle(revolutionsPerSecond)
					self.setThrottle(throttle)
				
					

				
				if not self.everSeenMagnet:
					#set wheel position to 0 and adjust target accordingly
					if target>0:
						target-=self.wheelPosition
					if target<=0:
						target+=self.wheelPosition
					self.wheelPosition=0
				seenMagnet=True
				self.everSeenMagnet=True
				lastSeenMagnet=time.time()
					


		


	
