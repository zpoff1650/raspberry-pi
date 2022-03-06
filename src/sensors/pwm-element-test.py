# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time
import PiUtils

# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)



# Define variables
gpioPWMIndex = 33 # GPIO 13




print ("Setting up pins...")
PiUtils.setupGPIOPin(gpioPWMIndex, GPIO.OUT) # PWM Pin
pwmPin = GPIO.PWM(gpioPWMIndex, 100)
pwmPin.start(0)
print ("Pin Setup Complete")




def performPWMTest():
	# Loop through duty options

	dutyInc = 25
	dutyStageDuration = 20
	currentDuty = 0
	dutyMax = 100;

	while currentDuty < dutyMax:
		currentDuty += dutyInc
		print("Running at duty " + str(currentDuty) + " for " + str(dutyStageDuration) + " seconds.")
		pwmPin.ChangeDutyCycle(currentDuty)
		time.sleep(dutyStageDuration)





if __name__ == "__main__":
	try:
        	performPWMTest()
	except KeyboardInterrupt:
        	# Cleanup
        	GPIO.cleanup()
        	print ("Test Complete. Goodbye!")
	finally:
        	# Cleanup
        	GPIO.cleanup()
        	print ("Test Complete. Goodbye (Finally)!")



