## Raspberry Pi Util File
import RPi.GPIO as GPIO
import time



## Set verbose to false at initialization
VERBOSE_OPTION=False

def setVerbose(verboseValue):
    print("Setting verbose to " + str(verboseValue))
    VERBOSE_OPTION=verboseValue

def verbose():
    setVerbose(True)

def debug(message):
    if VERBOSE_OPTION:
        print("[DEBGU]: " + message)







def getGPIOPinSetupTypeDescription(setupType):
    if setupType is None:
        debug("setupType passed to GPIO pin is null")
        return "Omitted"
    
    setupTypeDescription = "UNKNOWN SETUP TYPE"
    if setupType == 0:
        setupTypeDescription = "GPIO.OUT"
    elif setupType == 1:
        setupTypeDescription = "GPIO.INPUT"
    else:
        print("Unknown setup type value: " + str(setupType))
    return setupTypeDescription



def getGPIOPinPUDTypeDescription(pudType):
    if pudType is None:
        debug("pudType passed to GPIO pin is null")
        return "Omitted"
    
    pudTypeDescription = "UNKNOWN PUD TYPE"
    if pudType == 0:
        # Will set button press/input action to True
        setupTypeDescription = "GPIO.PUD_UP"
    elif pudType == 1:
        # Will set button press/input action to False
        setupTypeDescription = "GPIO.PUD_DOWN"
    else:
        print("Unknown setup type value: " + str(setupType))
    
    return pudTypeDescription


def setupGPIOPinWithPUDType(gpioPinIndex, setupType, pudType):
    if VERBOSE_OPTION:
        setupTypeDescription = getGPIOPinSetupTypeDescription(setupType)
        pudTypeDescription = getGPIOPinPUDTypeDescription(pudType)
        
        if pudType is None:
            print ("Setting up pin " + str(gpioPinIndex) + " as type " + setupTypeDescription)
        else:
            print ("Setting up pin " + str(gpioPinIndex) + " as type " + setupTypeDescription + " with PUD type " + pudTypeDescription)
    
    if pudType is None:
        GPIO.setup(gpioPinIndex, setupType)
    else:
        GPIO.setup(gpioPinIndex, setupType, pull_up_down=pudType)


def setupGPIOPin(gpioPinIndex, setupType):
    setupGPIOPinWithPUDType(gpioPinIndex, setupType, None)


def commonDestroy():
    if verboseOption:
        print("Cleaning up GPIO pins")
    # Cleanup
    GPIO.cleanup()
    if verboseOption:
        print("GPIO pin cleanup complete!")
    





### LED TESTING FUNCTIONS
    
# LONGER SIDE OF LEDs NEED TO CONNECT TO THE + (positive) TERMINAL

# Bightness is a logarithmic function so the values are 1, 2, 4, 8, 16, 32, 64 (probably more). This means that duty 2 is twice as bright as duty 1 and duty 64 is 7x brighter than duty 1
ledBrightnessValues = [1, 2, 4, 8, 16, 32, 64]

def getBrightnessDutyFromBrightnessValue(brightnessValue):
    # Subtract 1 from value as indexes start at 0 but brightness level starts at 1
    return ledBrightnessValues[brightnessValue-1]
    

def testLEDBrightness(pwmLEDIndex, secondsBetweenChanges, brightnessValuesToLoopThrough):
    for brightnessDuty in brightnessValuesToLoopThrough:
        debug("Using duty " + str(brightnessDuty))
        pwmLEDIndex.ChangeDutyCycle(brightnessDuty)
        time.sleep(secondsBetweenChanges)


def testLEDBrightnessDimToBright(pwmLED, secondsBetweenChanges):
    debug("Looping through LED brightness values from dim to bright with " + str(secondsBetweenChanges) + " seconds between changes")
    testLEDBrightness(pwmLED, secondsBetweenChanges, ledBrightnessValues)


def testLEDBrightnessBrightToDim(pwmLED, secondsBetweenChanges):
    debug("Looping through LED brightness values from bright to dim with " + str(secondsBetweenChanges) + " seconds between changes")
    testLEDBrightness(pwmLED, secondsBetweenChanges, reversed(ledBrightnessValues))
    

def turnLEDOn(gpioLEDIndex):
    debug("Turning LED at index " + str(gpioLEDIndex) + " ON")
    GPIO.output(gpioLEDIndex, True)


def turnLEDOff(gpioLEDIndex):
    debug("Turning LED at index " + str(gpioLEDIndex) + " OFF")
    GPIO.output(gpioLEDIndex, False)    

def setLEDToBrightness(brightness, gpioLEDIndex):
    if brightness is None or brightness < 0 or brightness > 7:
        print("Brightness value required to be int between 1 and 7")
        
    debug("Setting LED at index " + str(gpioLEDIndex) + " to brightness level " + str(brightness))

    if brightness == 0:
        turnLEDOff(gpioLEDIndex)

    else:
        # Ensure light is on
        turnLEDOn(gpioLEDIndex)
        
        # Set duty to brightness
        gpioLEDIndex.ChangeDutyCycle(getBrightnessDutyFromBrightnessValue(brightness))
    


# Define GPIO Test Cases
def performGeneralLEDTest(gpioLEDIndex):
    numebrOfBlinksForTest = 3
    timeBetweenBlinks = 0.5
    
    debug("Performing general LED test for LED at index " + str(gpioLEDIndex) + ". Light with blink " + str(numebrOfBlinksForTest) + " times with " + str(timeBetweenBlinks) + " seconds on and off")
    
    # Blink LED 3 times
    for x in range(numebrOfBlinksForTest):
        turnLEDOn(gpioLEDIndex)
        time.sleep(timeBetweenBlinks)
        turnLEDOff(gpioLEDIndex)
        time.sleep(timeBetweenBlinks)
    debug("General LED at index " + str(gpioLEDIndex) + ".")







## MOTOR UTILS
def getMotorDescription(gpioMotorForward, gpioMotorBackward):
    return "(" + str(gpioMotorForward) + "," + str(gpioMotorBackward) + ")";

def motorForward(gpioMotorForward, gpioMotorBackward):
    debug("Moving motor " + getMotorDescription(gpioMotorForward, gpioMotorBackward) + " FORWARD")
    GPIO.output(gpioMotorForward, True)
    GPIO.output(gpioMotorBackward, False)

def motorBackward(gpioMotorForward, gpioMotorBackward):
    debug("Moving motor " + getMotorDescription(gpioMotorForward, gpioMotorBackward) + " BACKWARD")
    GPIO.output(gpioMotorBackward, True)
    GPIO.output(gpioMotorForward, False)

def motorStop(gpioMotorForward, gpioMotorBackward):
    debug("Stopping motor " + getMotorDescription(gpioMotorForward, gpioMotorBackward))
    GPIO.output(gpioMotorForward, False)
    GPIO.output(gpioMotorBackward, False)







## LINEAR ACTUATOR UTILS
ACTUATOR_TIME_TO_COLLAPSE_VALUE = 8
ACTUATOR_FULL_SPEED_CYCLE_VALUE = 1
ACTUATOR_OFF_CYCLE_VALUE = 100
def moveActuatorIn(gpioActuatorPWMIN1, gpioActuatorPWMIN2, speed):
    debug("Moving actuator at " + str(gpioActuatorPWMIN2) + " IN")
    gpioActuatorPWMIN1.ChangeDutyCycle(ACTUATOR_OFF_CYCLE_VALUE) # Change duty cycle to min value (100)
    gpioActuatorPWMIN2.ChangeDutyCycle(speed) # Change duty cycle to requested speed


def moveActuatorOut(gpioActuatorPWMIN1, gpioActuatorPWMIN2, speed):
    debug("Moving actuator at " + str(gpioActuatorPWMIN1) + " OUT")
    gpioActuatorPWMIN1.ChangeDutyCycle(speed) # Change duty cycle to requested speed 
    gpioActuatorPWMIN2.ChangeDutyCycle(ACTUATOR_OFF_CYCLE_VALUE) # Change duty cycle to min value (100)


def actuatorStop(gpioActuatorPWMIN1, gpioActuatorPWMIN2):
    gpioActuatorPWMIN1.ChangeDutyCycle(ACTUATOR_OFF_CYCLE_VALUE) # Change duty cycle to min value (100)
    gpioActuatorPWMIN2.ChangeDutyCycle(ACTUATOR_OFF_CYCLE_VALUE) # Change duty cycle to min value (100)

def fullyExpandActuator(gpioActuatorPWMIN1, gpioActuatorPWMIN2):
    debug("Expanding actuator...")
    moveActuatorOut(gpioActuatorPWMIN1, gpioActuatorPWMIN2, ACTUATOR_FULL_SPEED_CYCLE_VALUE)
    for x in range(ACTUATOR_TIME_TO_COLLAPSE_VALUE):
        time.sleep(1)
        debug("Expand time: " + str(x))
    debug("Actuator expanded")

def fullyCollapseActuator(gpioActuatorPWMIN1, gpioActuatorPWMIN2):
    debug("Collapsing actuator...")
    moveActuatorIn(gpioActuatorPWMIN1, gpioActuatorPWMIN2, ACTUATOR_FULL_SPEED_CYCLE_VALUE)
    for x in range(ACTUATOR_TIME_TO_COLLAPSE_VALUE):
        time.sleep(1)
        debug("Collapse time: " + str(x))
    debug("Actuator collapsed")


