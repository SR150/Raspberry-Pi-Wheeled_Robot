import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class reedSwitch:
	pin=0
	on=False
	minimumTimeBetweenOn=0.1
	lastTimeOn=0
	def __init__(self,pin):
		self.pin=pin
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
		self.on=GPIO.input(self.pin)== GPIO.HIGH
		
	def pollState(self):
		buttonOnNow=GPIO.input(self.pin)== GPIO.HIGH
		if self.on and buttonOnNow:
			self.lastTimeOn=time.time()
			return False
			
		if not self.on and buttonOnNow:
			self.lastTimeOn=time.time()
			self.on=True
			return True
			
		if self.on and not buttonOnNow and time.time()-self.lastTimeOn>self.minimumTimeBetweenOn:
			self.on=False
			
		return False


if __name__=="__main__":
	switch=reedSwitch(14)#button 22 left 14 right 21
	import time
	while True:
		print(switch.pollState())
		time.sleep(1)
		
