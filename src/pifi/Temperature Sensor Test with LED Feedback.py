# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time


import board
import adafruit_dht
## To run this, you must install the library in the terminal using "sudo pip3 install Adafruit_DHT"

import PiUtils as PiUtils


# Define variables
gpioLEDIndex = 40 # Last one on the outside by the USB ports
dhtDevice = adafruit_dht.DHT11(board.D4) # This is pin 7 or GPIO4



def lightON():
    PiUtils.turnLEDOn(gpioLEDIndex)

def lightOFF():
    PiUtils.turnLEDOff(gpioLEDIndex)


def initGPIOPins():
    print ("Setting up pins...")
    PiUtils.setupGPIOPin(gpioLEDIndex, GPIO.OUT) # LED Indicator
    print ("Pin Setup Complete")
    

def performTemperatureSensorTestWithLEDFeedback():
    ## Start infinite loop with sensor dection causing LED to shine
    print("Starting motion test. Press Ctrl+C to exit.")
    
    PiUtils.setVerbose(False)
    
    # Time Duration in seconds
    timeDuration=60
    
    # Motion Counte
    motionsDetected=0
    
    print("Starting temperature detection for " + str(timeDuration) + " seconds...")
    
    lightON()
    startTime=time.time()
    while time.time()-startTime < timeDuration:
            
        try: 
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            
            if humidity is not None and temperature_c is not None:
                
                temperature_f = temperature_c * (9 / 5) + 32
                
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        temperature_f, temperature_c, humidity
                    )
                )
            elif humidity is None and temperature_c is None:
                print("Failed to detect temperature and humidity. Check wiring")
            elif humidity is None:
                print("Failed to detect humidity. Sensor.")
            else:
                print("Failed to detect temperature. Sensor.")
                

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        ## Can only read one time per second
        time.sleep(2.0)
    
    
    
    
    print("Temperature detection completed.")
    lightOFF()
    

# Setup output pins for motor
try:
    PiUtils.verbose()
    
    # Init GPIO Pins
    initGPIOPins()
    
    # Verify LED pin setup before testing motor with LED feedback
    PiUtils.performGeneralLEDTest(gpioLEDIndex)
    
    performTemperatureSensorTestWithLEDFeedback()
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")



