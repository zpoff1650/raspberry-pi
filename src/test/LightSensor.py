import time
import RPi.GPIO as GPIO


# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)



testLoopCount = 100
capacitorIndex = 40


GPIO.setup(capacitorIndex, GPIO.OUT)

def getBrightnessLevelDescription(brightnessLevel):
    if brightnessLevel == 1:
        return 'Very Dark'
    elif brightnessLevel == 2:
        return 'Dark'
    elif brightnessLevel == 3:
        return 'Pretty Bright'
    elif brightnessLevel == 4:
        return 'Bright'
    else:
        return 'Very Bright'
    

def getBrightnessLevelFromChargeTime(timeDiff):
    if timeDiff >= 1000:
        return 1
    elif timeDiff >= 500:
        return 2
    elif timeDiff >= 100:
        return 3
    elif timeDiff >= 50:
        return 4
    else:
        return 5


def getBrightnessLevel():
    startTime = time.time()
    
    # Set capacitor to low
    GPIO.setup(capacitorIndex, GPIO.OUT)
    GPIO.output(capacitorIndex, GPIO.LOW)
    
    # Ensure discharged
    timeDiff = 0
    while (GPIO.input(capacitorIndex) == GPIO.HIGH):
        timeDiff = time.time() - startTime
    print('Discharge time: ' + str(timeDiff * 1000))
    
    
    #Change the pin back to input
    GPIO.setup(capacitorIndex, GPIO.IN)
   
   
    timeDiff = 0
    #Count until the pin goes high
    while (GPIO.input(capacitorIndex) == GPIO.LOW):
        timeDiff = time.time() - startTime
    
    timeDiffMilliseconds = timeDiff * 1000
    print('Charge time: ' + str(timeDiffMilliseconds))
    
    return getBrightnessLevelFromChargeTime(timeDiffMilliseconds)


def testSensor():
    try:
        print('Starting capacitor test...')
        loopCount = 0
        while loopCount < testLoopCount:
            print('Starting Loop ' + str(loopCount))
            
            print(getBrightnessLevelDescription(getBrightnessLevel()))


            loopCount += 1
            time.sleep(1)
            
    finally:
        GPIO.cleanup()
        print('Good Bye')


