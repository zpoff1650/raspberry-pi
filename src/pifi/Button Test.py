# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

# Define board numbering mode
GPIO.setmode(GPIO.BOARD)


# Setup output pins for motor
GPIO.setup(7, GPIO.IN)

print ('Test Ready...')

try:
    while True:
        if not GPIO.input(7):
            print ('Button Input Received')
        else:
            print ('Nothing')
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")



