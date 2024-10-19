import RPi.GPIO as GPIO
import time
class motor:
	def __init__(self,forwards,backwards):
		GPIO.setmode(GPIO.BCM)
		
		GPIO.setup(forwards, GPIO.OUT)
		GPIO.setup(backwards, GPIO.OUT)
		
		

		self.forwardsPin=GPIO.PWM(forwards,100)
		self.backwardsPin=GPIO.PWM(backwards,100)

		self.forwardsPin.start(0)
		self.backwardsPin.start(0)
		self.setThrottle(0)


	def setThrottle(self,throttle):
		if throttle>0:
			self.forwardsPin.ChangeDutyCycle(throttle*100)
			self.backwardsPin.ChangeDutyCycle(0)
		else:
			self.forwardsPin.ChangeDutyCycle(0)
			self.backwardsPin.ChangeDutyCycle(-throttle*100)
	def __del__(self):
		self.setThrottle(0)
		self.forwardsPin.stop()
		self.backwardsPin.stop()
		
		
		
if __name__=="__main__":
	left=motor(23,24)
	right=motor(8,25)

	
	left.setThrottle(00)
	right.setThrottle(00)
