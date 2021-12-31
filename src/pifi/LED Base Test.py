# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define variables
gpioLEDIndex = 40 #Last one on the outside by the USB ports


def initGPIOPins():
    print ("Setting up pins...")
    GPIO.setup(gpioLEDIndex, GPIO.OUT) # LED Indicator
    print ("Pin Setup Complete")



def performLEDTest(gpioLEDIndex):
    # Blink LED 5 times
    for x in range(5):
        GPIO.output(gpioLEDIndex, True)
        time.sleep(0.5)
        GPIO.output(gpioLEDIndex, False)
        time.sleep(0.5)



# Setup output pins for motor
try:
    initGPIOPins()
    print ("Testing LED...")
    performLEDTest(gpioLEDIndex)
    print ("LED Test Complete")
    
    
    
    
    
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")
