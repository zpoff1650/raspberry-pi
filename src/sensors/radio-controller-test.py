# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time
import PiUtils

# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)




gpioRadioInputIndex = 31 #GPIO 6
gpioMotorForward = 11
gpioMotorBackward = 13



def initGPIOPins():
    print ("Setting up pins...")
    PiUtils.setupGPIOPin(gpioRadioInputIndex, GPIO.IN) # Throttle? Channle 3 on the receiver
    PiUtils.setupGPIOPin(gpioMotorForward, GPIO.OUT) # IN1 Forward
    PiUtils.setupGPIOPin(gpioMotorBackward, GPIO.OUT) # IN2 Backward
    print ("Pin Setup Complete")









def runRadioSensor():
    print("Running radio sensor...")
    while True:
        if GPIO.input(gpioRadioInputIndex) == True:
            print("Input True: " + str(GPIO.input(gpioRadioInputIndex)))
            GPIO.output(gpioMotorForward, True)
        else:
            print("Stopping Motor: " + str(GPIO.input(gpioRadioInputIndex)))
            GPIO.output(gpioMotorForward, False)









if __name__ == "__main__":
    try:
        # Init GPIO Pins
        initGPIOPins()

        runRadioSensor()
    except KeyboardInterrupt:
        # Cleanup
        GPIO.cleanup()
        print ("Test Complete. Goodbye!")
    finally:
        # Cleanup
        GPIO.cleanup()
        print ("Test Complete. Goodbye (Finally)!")


