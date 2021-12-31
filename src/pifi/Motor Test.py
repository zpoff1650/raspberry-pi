# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

# Define board numbering mode
GPIO.setmode(GPIO.BOARD)


# Setup output pins for motor
try:
    print ("Setting up pins...")
    GPIO.setup(11, GPIO.OUT) # IN1 Forward
    GPIO.setup(12, GPIO.OUT) # IN2 Backward
    print ("Pin setup complete")

    print ("Step 1: Going forward in 5 seconds, for 2 seconds...")
    time.sleep(5)
    GPIO.output(11, True)
    time.sleep(5)
    GPIO.output(11, False)
    print ("Step 1 complete.")

    print ("Step 2: Going backward in 5 seconds, for 2 seconds...")
    time.sleep(5)
    GPIO.output(12, True)
    time.sleep(5)
    GPIO.output(12, False)
    print ("Step 2 complete.")
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")

