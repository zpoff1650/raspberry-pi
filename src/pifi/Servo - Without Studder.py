# Import Required Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output for the servo
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # Note, 11 is the pin, 55 = 50Hz pulse for controlling servo

# Start PWM running, but with value 0 (pulse off)
servo1.start(0)
print("Waiting 2 seconds ")
time.sleep(2)

# Let's move the servo!
print ("Rotating 180 degrees in 10 steps")


duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    # 0.3 is a close estimate to how long it takes for the servo to move 18 degrees (1/10th of 180 degrees)
    time.sleep(0.3)
    # Tell servo to stop trying to figure out/correct it's location
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1
    
time.sleep(2)


print ("Turnning back to 90 degress for 2 seconds")
servo1.ChangeDutyCycle(7)
time.sleep(2)

# Turn back to 0
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Cleanup
servo1.stop()
GPIO.cleanup()
print ("Test Complete")









