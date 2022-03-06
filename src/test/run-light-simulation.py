import time
import re
from datetime import datetime
import UserInputUtil as UIU
import RPi.GPIO as GPIO
import PinConfiguration as PCI
import LogUtil
import LightSensor



# REQUIREMENTS
# -Light
#  * 12v Battery
#  * LED(s) with resistors for 12v power supply
#  * Transistor 2n2222a
#  * 1 GPIO Data pin
#  * 1 3.3v GPIO pin
#  * 1 Common Groupd GPIO pin
# -Light Sensor
#  * 1 photoresistor
#  * 1 GPIO Data pin
#  * 1 10uf capacitor
#  * 1 Common Groupd GPIO pins
# 
# WIRING
# -Light
# 12v [+] to the [+] diode of the LED(s)/resistor rig. [-]  of LED rig to right side of transistor when flat-side is facing you/up.
# Middle diode of transistor goes to one GPIO data pin for control light switch. Left side of transistor diode connects to common ground GPIO pin as well as the 12v [-] diode.
# This requires splitting that connection multiple times.
# 
# -Light Sensor
# GPIO 3.3v pin to photoresistor. Photoresistor to [+] capacitor diode with GPIO data pin connecting inside of this segment. [-] capacitor diode connects to common ground.
# 
# 
# 
# 
# 





















# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)

# CONSTANTS
LOGGER = LogUtil.getNewLogger('light_simulation_service')
MODE_START_AND_END_TIME = 'START_AND_END_TIME'
MODE_HOURS_PER_DAY = 'HOURS_PER_DAY'
DEFAULT_SECONDS_BETWEEN_PROBES = 30
DEFAULT_BRIGHTNESS_THRESHOLD = 3 # Pretty Bright+
SIMULATION_STATE_DESCRIPTION = 'Uninitialized'

# Configuration Variables
LIGHT_SIMULATION_MODE = ''

## Start and end time mode
START_TIME_EACH_DAY = None
END_TIME_EACH_DAY = None

## Start and end time mode
HOURS_PER_DAY = None



def processGameModeDecision(modeStartAndEndTimeFunction, hoursPerDayFunction):
    global LIGHT_SIMULATION_MODE, MODE_START_AND_END_TIME, MODE_HOURS_PER_DAY
    if MODE_START_AND_END_TIME == LIGHT_SIMULATION_MODE:
        modeStartAndEndTimeFunction()
    elif MODE_HOURS_PER_DAY == LIGHT_SIMULATION_MODE:
        hoursPerDayFunction()
    else:
        print('Failed to locate light simulation mode: "' + LIGHT_SIMULATION_MODE + "'")

def configureStartAndEndTimeSimulation():
    global START_TIME_EACH_DAY, END_TIME_EACH_DAY, SIMULATION_STATE_DESCRIPTION
    SIMULATION_STATE_DESCRIPTION = 'Configuring Start and End Time simulation mode'
    # Track state for debugging
    logStateDescription()
    START_TIME_EACH_DAY = UIU.getUserTimeInput('Start time? ')
    LOGGER.info('Start time configured to: ' + str(START_TIME_EACH_DAY))
    END_TIME_EACH_DAY = UIU.getUserTimeInput('End time? ')
    LOGGER.info('End time configured to: ' + str(END_TIME_EACH_DAY))
    
def configureHoursPerDaySimulation():
    global HOURS_PER_DAY, SIMULATION_STATE_DESCRIPTION
    SIMULATION_STATE_DESCRIPTION = 'Configuring Hours Per Day simulation mode'
    # Track state for debugging
    logStateDescription()
    HOURS_PER_DAY = UIU.getUserNumberInput('How many hours of light per day? ')
    LOGGER.info('Hours per day configured to: ' + str(HOURS_PER_DAY))
    SUN_RISE_SUN_SET_ATTATCHMENT_MODE = UIU.getUserNumberInput('Attach to sun rise or sun set? ')
    LOGGER.info('Hours per day configured to: ' + str(HOURS_PER_DAY))

def logStateDescription():
    LOGGER.info('(SS): ' + SIMULATION_STATE_DESCRIPTION)

def configureLightSimulation():
    print('Configuring Simulation...')
    GPIO.setup(PCI.LIGHTS_TRANSISTOR_SIGNAL_PIN_INDEX, GPIO.OUT)
    
    # Set light simulation mode
    global LIGHT_SIMULATION_MODE, PROBE_FREQUENCY, DEFAULT_BRIGHTNESS_THRESHOLD
    LIGHT_SIMULATION_MODE = UIU.getUserInputFromList('Which mode should be run? ', [MODE_START_AND_END_TIME, MODE_HOURS_PER_DAY])
    LOGGER.info('Light Simulation Mode configured to: ' + str(LIGHT_SIMULATION_MODE))
    
    # Set configuration based on light simulation mode
    processGameModeDecision(configureStartAndEndTimeSimulation, configureHoursPerDaySimulation)
    
    PROBE_FREQUENCY = UIU.getUserNumberInputWithEmptyDefault('How many seconds between soil sensor probes? Empty for default ' + str(DEFAULT_SECONDS_BETWEEN_PROBES) + ' meaning 2 probes per minute: ', DEFAULT_SECONDS_BETWEEN_PROBES)
    LOGGER.info('Probe Frequency configured to: ' + str(PROBE_FREQUENCY))
    
    DEFAULT_BRIGHTNESS_THRESHOLD = UIU.getUserNumberInputWithEmptyDefault('What brightness threshold would you like? Empty for default ' + str(DEFAULT_BRIGHTNESS_THRESHOLD) + ' meaning if the light should be on and the brightness is found to be darker than ' + str(DEFAULT_BRIGHTNESS_THRESHOLD) + ' artificial lighting will engage: ', DEFAULT_BRIGHTNESS_THRESHOLD)
    LOGGER.info('Probe Frequency configured to: ' + str(PROBE_FREQUENCY))
    
    print('Simulation Configured')



def turnLightOn(ledIndex):
    brightnessLevel = LightSensor.getBrightnessLevel()
    if brightnessLevel < DEFAULT_BRIGHTNESS_THRESHOLD:
        GPIO.output(ledIndex, True)
        LOGGER.info('Brightness level "' + LightSensor.getBrightnessLevelDescription(brightnessLevel)
                    + '" is less than threshold "' + LightSensor.getBrightnessLevelDescription(DEFAULT_BRIGHTNESS_THRESHOLD) + '". Using artificial LED light')
    else:
        GPIO.output(ledIndex, False)
        LOGGER.info('Brightness level "' + LightSensor.getBrightnessLevelDescription(brightnessLevel)
                    + '" is greater than threshold "' + LightSensor.getBrightnessLevelDescription(DEFAULT_BRIGHTNESS_THRESHOLD) + '" and thus bright enough.')
    


def runStartAndEndTimeSimulation():
    global START_TIME_EACH_DAY, END_TIME_EACH_DAY, SIMULATION_STATE_DESCRIPTION
    # Turn on light during defined start and end times
    while True:
        currentTime = datetime.now().time()
        # Log simulation data
        if currentTime >= START_TIME_EACH_DAY and currentTime <= END_TIME_EACH_DAY:
            # Trun light on
            turnLightOn(PCI.LIGHTS_TRANSISTOR_SIGNAL_PIN_INDEX)
            # Update simulation state description for logger
            SIMULATION_STATE_DESCRIPTION = 'Light on'
        else:
            # Trun light off
            GPIO.output(PCI.LIGHTS_TRANSISTOR_SIGNAL_PIN_INDEX, False)
            # Update simulation state description for logger
            SIMULATION_STATE_DESCRIPTION = 'Light off'
        
        # Track state for debugging
        logStateDescription()
        time.sleep(PROBE_FREQUENCY)



def runHoursPerDaySimulation():
    print('TODO runHoursPerDaySimulation')
    ### Determine when the timer should start each day.
    # As soon as the sun rises? Not sure if this is really needed
    
    
    
    


def runLightSimulation():
    print('Running Light Simulation...')
    configureLightSimulation()
    
    print('Running simulation. Press Ctrl+C to end simulation at any time.')
    processGameModeDecision(runStartAndEndTimeSimulation, runHoursPerDaySimulation)

    





try:
    runLightSimulation()
finally:
    # Cleanup
    GPIO.cleanup()
    print('End Light Simulation')

