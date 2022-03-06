# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

import PiUtils as PiUtils

# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)


## REQUIRES MOTOR CONTROLLER AND 12V BATTERY


# Define variables
gpioLEDIndex = 40 # Last one on the outside by the USB ports
gpioMotorForward = 11 # 6th in on the inside starting away from USB ports
gpioMotorBackward = 12 # 6th in on the outside starting away from USB ports


def lightON():
    PiUtils.turnLEDOn(gpioLEDIndex)

def lightOFF():
    PiUtils.turnLEDOff(gpioLEDIndex)

def initGPIOPins():
    print ("Setting up pins...")
    PiUtils.setupGPIOPin(gpioLEDIndex, GPIO.OUT) # LED Indicator
    PiUtils.setupGPIOPin(gpioMotorForward, GPIO.OUT) # IN1 Forward
    PiUtils.setupGPIOPin(gpioMotorBackward, GPIO.OUT) # IN2 Backward
    print ("Pin Setup Complete")




def performLinearActuatorTestWithLEDFeedback():
    ## Change Directions: NO idea other than reverse +/- wiring
    ## Change Speed: Lower duty cycle (1) seems to be the fastest whereas highest duty cycle (100) seems to be stopped
    ## FREQUENCY seems to just change the sound and the "Best" sound right now appears to be 100. I'm guessing there is a correct value here
    
    
    
    # AT STARTUP (-=OUT1, +=OUT2) THE ACTUATOR MOVES IN/COLLAPSES
    
    
    ## Using custom logging
    #PiUtils.setVerbose(False)
    
    
    # Setup PWM
    pwmFrequency = 100 ## Seems to dictate sound of motor. Currently 100 sounds the best
    dutyCycle = 100
    
    print ("Initializing GPIO PWM pin " + str(gpioMotorForward) + " to frequency " + str(pwmFrequency) + " with duty cycle " + str(dutyCycle))
    pwmForward = GPIO.PWM(gpioMotorForward, pwmFrequency)
    pwmForward.start(dutyCycle)
    
    print ("Initializing GPIO PWM pin " + str(gpioMotorBackward) + " to frequency " + str(pwmFrequency) + " with duty cycle " + str(dutyCycle))
    pwmBackward = GPIO.PWM(gpioMotorBackward, pwmFrequency)
    pwmBackward.start(dutyCycle)
    
    
    sleepTimeAfterLog = 0.5
    testCycleTime = 3
    
    ## Init test with motor indexes to false
    PiUtils.actuatorStop(pwmForward, pwmBackward)
    print ("Testing Linear Actuator...")
    
    #PiUtils.fullyCollapseActuator(pwmForward, pwmBackward);
    
    
    
    print ("Moving out")
    PiUtils.moveActuatorOut(pwmForward, pwmBackward, 1)
    time.sleep(testCycleTime)
    print ("Stop")
    print ("Moving in")
    PiUtils.moveActuatorIn(pwmForward, pwmBackward, 1)
    time.sleep(testCycleTime)
    print ("Stop")
    
    
    print ("Fully extending")
    PiUtils.fullyExpandActuator(pwmForward, pwmBackward)
    print ("Hold for 3")
    time.sleep(3)
    print ("Stop")
    PiUtils.fullyCollapseActuator(pwmForward, pwmBackward)
    print ("Fully collapsing")
    
    
    
    print ("Stop")
    PiUtils.actuatorStop(pwmForward, pwmBackward)
    

    print ("Going to Extend for 30 seconds for measuring...")
    PiUtils.fullyExpandActuator(pwmForward, pwmBackward)
    print ("Holding for 30 seconds")
    time.sleep(30)
    print("Done. Collapsing")
    PiUtils.fullyCollapseActuator(pwmForward, pwmBackward)
    print("Done")
    
    

# Setup output pins for motor
try:
    # Set utils to verbose to log actions
    PiUtils.verbose()
    
    # Init GPIO Pins
    initGPIOPins()
    
    # Verify LED pin setup before testing motor with LED feedback
    PiUtils.performGeneralLEDTest(gpioLEDIndex)
    
    
    performLinearActuatorTestWithLEDFeedback()
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")

