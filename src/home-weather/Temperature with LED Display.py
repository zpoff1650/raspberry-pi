# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time
import datetime


import board
import adafruit_dht # To run this, you must install the library in the terminal using "sudo pip3 install Adafruit_DHT


import LCD1602
import time


# WIRING
#
# Sensor: 5v and data to pin 7/GPIO04
# LCD: 5V then next pin goes to SDA1 and final goes to SCL1



# LCD Functions
def writeToLCD(line1Text, line2Text):
    # LCD line is 16 length
    maxLineLength = 15 # 16 places but starts with index 0
    print("Writing to LCD Display: [{}] [{}]".format(line1Text, line2Text))
    
    line1TextLength=len(line1Text)
    line2TextLength=len(line2Text)
    
    line1EndIndex = line1TextLength
    
    if line1EndIndex > maxLineLength:
        # This line will need to scroll
        line1EndIndex = maxLineLength
        
    line2EndIndex = line2TextLength
       
    if line2EndIndex > maxLineLength:
        # This line will need to scroll
        line2EndIndex = maxLineLength 
    
    
    line1StartIndex=0
    line2StartIndex=0
    
    # Iniitalize display to the beginning of each line's text    
    LCD1602.write(0, 0, line1Text[line1StartIndex:line1EndIndex])
    LCD1602.write(1, 1, line2Text[line2StartIndex:line2EndIndex])
    
    while line1EndIndex < line1TextLength or line2EndIndex < line2TextLength:
        
        if line1EndIndex < line1TextLength and line1TextLength >= maxLineLength:
            # Scroll Line
            line1StartIndex+=1
            line1EndIndex+=1
        
        if line2EndIndex < line2TextLength and line2TextLength >= maxLineLength:
            # Scroll Line
            line2StartIndex+=1
            line2EndIndex+=1
        
        
        #print("Writing {} to line 1".format(line1Text[line1StartIndex:line1EndIndex]))
        #print("Writing {} to line 2".format(line2Text[line2StartIndex:line2EndIndex]))
        LCD1602.write(0, 0, line1Text[line1StartIndex:line1EndIndex])
        LCD1602.write(1, 1, line2Text[line2StartIndex:line2EndIndex])
        
        
        # Controls scroll speed
        time.sleep(0.5)
    
    
    
    
    

def setupLCD():
    LCD1602.init(0x27, 1)   # init(slave address, background light)
    writeToLCD('Greetings!', 'You dim fucker')
    time.sleep(2)

def destroyLCD():
    LCD1602.clear()
    
# Define variables

def initGPIOPins():
    print ("Setting up pins...")
    print ("Pin Setup Complete")


def displayTemperatureAndHumidityOnLCD(timeNow, temperature_f, temperature_c, humidity):
    humidityLine = str(timeNow) + " Humidity: " + str(humidity) + "%"
    tempLine = "Temp: " + str(temperature_f) + "F " + str(temperature_c) + "C"
    writeToLCD(humidityLine, tempLine)
    
    


def startTemperatureAndHumiditySensor():
    # Start infinite loop with sensor
    writeToLCD("Starting temperature and humiditiy sensor.", "Press Ctrl+C to exit.")
    dhtDevice = adafruit_dht.DHT11(board.D4) # This is pin 7 or GPIO4 for the temperature and humidity sensors combined
    time.sleep(2.0)
    
    
    while True:
        # writeToLCD("Reading from sensors...", "Press Ctrl+C to exit.")
        try: 
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            # writeToLCD("Raw data: {} {}".format(temperature_c, humidity), "Press Ctrl+C to exit.")
            if humidity is not None and temperature_c is not None:
                temperature_f = temperature_c * (9 / 5) + 32
                
                # Log temperature
                dateTimeNow = datetime.datetime.now()
                dateTimeString = dateTimeNow.strftime('%I:%M %p')

                print(
                    "{}: Temp: {:.1f} F / {:.1f} C    Humidity: {}%".format(
                        dateTimeString, temperature_f, temperature_c, humidity
                    )
                )
                
                # Show data on LCD
                displayTemperatureAndHumidityOnLCD(dateTimeString, temperature_f, temperature_c, humidity)
                
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
    







if __name__ == "__main__":
    try:
        # Init GPIO Pins
        initGPIOPins()
        setupLCD()
        
        startTemperatureAndHumiditySensor()
    except KeyboardInterrupt:
        destroyLCD()
        # Cleanup
        GPIO.cleanup()
        print ("Test Complete. Goodbye!")
    finally:
        destroyLCD()
        # Cleanup
        GPIO.cleanup()
        print ("Test Complete. Goodbye (Finally)!")
        
    




