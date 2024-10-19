import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import subprocess
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


if __name__=="__main__":
	pin=22
	path="/media/sr/0ECE-CBF9"
	
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
	while True:
		if GPIO.input(pin) == GPIO.HIGH:
			print("button pressed")
			try:
				subprocess.run(["python3", path+"/main.py"])
			except Exception as e:
				try:
					file.open(path+"/error.txt","w")
					file.write(str(e))
					file.close()
				except:
					pass


	



