# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

import PiUtils as PiUtils

# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)


# Define variables
gpioLEDIndex = 40 # Last one on the outside by the USB ports
gpioMotionSensor = 5 # 3rd in on the inside starting away from USB ports


def lightON():
    PiUtils.turnLEDOn(gpioLEDIndex)

def lightOFF():
    PiUtils.turnLEDOff(gpioLEDIndex)


def initGPIOPins():
    print ("Setting up pins...")
    PiUtils.setupGPIOPin(gpioLEDIndex, GPIO.OUT) # LED Indicator
    PiUtils.setupGPIOPin(gpioMotionSensor, GPIO.IN) # IN1 Motion Detection
    print ("Pin Setup Complete")
    

def performMotionSensorTestWithLEDFeedback():
    ## Start infinite loop with sensor dection causing LED to shine
    print("Starting motion test. Press Ctrl+C to exit.")
    
    PiUtils.setVerbose(False)
    
    # Time Duration in seconds
    timeDuration=60
    
    # Motion Counter
    motionsDetected=0
    
    print("Starting motion detection for " + str(timeDuration) + " seconds...")
    
    startTime=time.time()
    while time.time()-startTime < timeDuration:
        if GPIO.input(gpioMotionSensor):
            print("Motion Detected!")
            lightON()
            if motionDetectionActive == False:
                motionsDetected += 1
            motionDetectionActive=True
        else:
            print("Listening...")
            lightOFF()
            motionDetectionActive=False
            
    
    print("Motion detection completed. " + str(motionsDetected) + " motions detected")
    
    
    

# Setup output pins for motor
try:
    PiUtils.verbose()
    
    # Init GPIO Pins
    initGPIOPins()
    
    # Verify LED pin setup before testing motor with LED feedback
    PiUtils.performGeneralLEDTest(gpioLEDIndex)
    
    
    performMotionSensorTestWithLEDFeedback()
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")


