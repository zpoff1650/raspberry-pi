# PWM Test File
import RPi.GPIO as GPIO
import time

import PiUtils as PiUtils



# Define board numbering mode and warnings
GPIO.setmode(GPIO.BOARD)
gpioPinIndex = 7



## LED Test Data
ledTestTimeBetweenDutyCycleChange = 1




try:
    # Set utils to verbose to log actions
    PiUtils.verbose()
    
    # Setup GPIO pins
    print ("Setting up pins...")
    # GPIO.setup(gpioPinIndex, GPIO.OUT)
    PiUtils.setupGPIOPin(gpioPinIndex, GPIO.OUT)
    print ("GPIO pin setup complete.")
    
    
    # Setup PWM
    pwmFrequency = 100 #10 millisecond cycle at 100hz (hertz)
    dutyCycle = 50 # Percentage of frequency where cycle is up and down.
    # 100hz frequency with a duty cycle of 50 will cause the pin to ready as HIGH for 5 millisconds and then LOW for 5 milliseconds (up for 5 milliseconds and then down for 5 milliseconds)
    
    print ("Initializing GPIO PWM pin " + str(gpioPinIndex) + " to frequency " + str(pwmFrequency) + " with duty cycle " + str(dutyCycle))
    pwmVal = GPIO.PWM(gpioPinIndex, pwmFrequency)
    pwmVal.start(dutyCycle)

    
    ## EXAMPLES
    # pwmVal.ChangeDutyCycle(10) # This will create one division so the PIO will output HIGH for 1 milliscond and then LOW for the last 9.
    # pwmVal.ChangeFrequency(200) # Example of changing initialized PWM frequency
    ### PWM pin output is PWM Frequency / Duty Cycle.
    ### For LEDs, changing the frequency doesn't change the brightness. Changing the duty cycle (to a higher value) will increase the brightness
    
    
    
    
    # Initialize LED Brightness test
    print("Initializing LED Brightness test...")
    PiUtils.testLEDBrightnessDimToBright(pwmVal, ledTestTimeBetweenDutyCycleChange)
    PiUtils.testLEDBrightnessBrightToDim(pwmVal, ledTestTimeBetweenDutyCycleChange)
    print("LED Brightness test complete")
    
    
    
    
    
    print("Deconstructing test")
    pwmVal.stop()


finally:
    PiUtils.commonDestroy();
    print ("Test Complete. Goodbye!")
    









