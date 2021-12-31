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
print("Waiting 2 seconds...")
time.sleep(2)
print("Setup Complete")


try:
    while True:
        # Ask user for desired servo angle
        angle = float(input("Enter angle between 0 & 180: "))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
finally:
    # Cleanup
    servo1.stop()
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")
    
        

















