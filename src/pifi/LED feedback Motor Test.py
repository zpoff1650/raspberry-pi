# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

import PiUtils as PiUtils

# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)



# Define variables
gpioLEDIndex = 40 # Last one on the outside by the USB ports
gpioMotorForward = 11 # 6th in on the inside starting away from USB ports
gpioMotorBackward = 12 # 6th in on the outside starting away from USB ports


def initGPIOPins():
    print ("Setting up pins...")
    PiUtils.setupGPIOPin(gpioLEDIndex, GPIO.OUT) # LED Indicator
    PiUtils.setupGPIOPin(gpioMotorForward, GPIO.OUT) # IN1 Forward
    PiUtils.setupGPIOPin(gpioMotorBackward, GPIO.OUT) # IN2 Backward
    print ("Pin Setup Complete")




def performMotorTestWithLEDFeedback():
    
    sleepTimeAfterLog = 0.5
    testCycleTime = 3
    
    print ("Testing Motor...")
    print ("Forward for " + str(testCycleTime) + " seconds...")
    time.sleep(sleepTimeAfterLog)
    
    PiUtils.turnLEDOn(gpioLEDIndex)
    PiUtils.motorForward(gpioMotorForward, gpioMotorBackward)
    time.sleep(testCycleTime)
    PiUtils.turnLEDOff(gpioLEDIndex)
    
    print ("Backward for " + str(testCycleTime) + " seconds...")
    time.sleep(sleepTimeAfterLog)
    
    PiUtils.turnLEDOn(gpioLEDIndex)
    PiUtils.motorBackward(gpioMotorForward, gpioMotorBackward)
    time.sleep(testCycleTime)
    PiUtils.turnLEDOff(gpioLEDIndex)
    
    print ("Stopping Motor")
    PiUtils.motorStop(gpioMotorForward, gpioMotorBackward)
    print ("Motor Test Complete")
    
    
    

# Setup output pins for motor
try:
    # Set utils to verbose to log actions
    PiUtils.verbose()
    
    # Init GPIO Pins
    initGPIOPins()
    
    # Verify LED pin setup before testing motor with LED feedback
    PiUtils.performGeneralLEDTest(gpioLEDIndex)
    
    
    performMotorTestWithLEDFeedback()
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")


