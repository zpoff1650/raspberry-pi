import time
import re
from datetime import datetime


import UserInputUtil



# CONSTANTS
MODE_START_AND_END_TIME = 'START_AND_END_TIME'
MODE_SUN_RISE_SUN_SET = 'SUN_RISE_SUN_SET'
DEFAULT_SECONDS_BETWEEN_PROBES = 30



def startLightSimulation():
    
    # Set light simulation mode
    lightSimulationMode = UserInputUtil.getUserInputFromList('Which mode should be run? ', [MODE_START_AND_END_TIME, MODE_SUN_RISE_SUN_SET])
    
    # Set configuration based on light simulation mode
    if MODE_START_AND_END_TIME == lightSimulationMode:
        # Need start and end time for when the light should be on
        startTimeEachDay = UserInputUtil.getUserTimeInput('Start time? ')
        endTimeEachDay = UserInputUtil.getUserTimeInput('End time? ')
    elif MODE_SUN_RISE_SUN_SET == lightSimulationMode:
        # TODO Use hours per day input and sun rise/set times to overlap as much as possible to save electricity and LEDs
        print('Implement it then...')
        
        # Set hours per day variable
        hoursPerDay = UserInputUtil.getUserNumberInput('How many hours of light per day? ')
    else:
        print('Failed to locate light simulation mode: ' + lightSimulationMode)
    
    
    probeFrequency = UserInputUtil.getUserNumberInputWithEmptyDefault('How many seconds between probes? Empty for default ' + str(DEFAULT_SECONDS_BETWEEN_PROBES) + ': ', DEFAULT_SECONDS_BETWEEN_PROBES)







try:
    startLightSimulation()
finally:
    print('End Light Simulation')

