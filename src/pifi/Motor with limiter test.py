# Import GPIOs and Time to wait
import RPi.GPIO as GPIO
import time

# Define board numbering mode
GPIO.setmode(GPIO.BOARD)

# Define variables
gpioLimiter = 7
gpioForward = 11
gpioBackward = 12
sleepTimer = 5
rollbackTimer = 0.2



# Setup output pins for motor
try:
    print ("Setting up pins...")
    GPIO.setup(gpioForward, GPIO.OUT) # IN1 Forward
    GPIO.setup(gpioBackward, GPIO.OUT) # IN2 Backward
    
    GPIO.setup(gpioLimiter, GPIO.IN) # Limiter switch
    print ("Pin setup complete")

    print ("Going forward until limiter detection in 5 seconds...")
    time.sleep(sleepTimer)
    GPIO.output(gpioForward, True)
    while GPIO.input(gpioLimiter):
        print ("No limiter detected")
        
    
    print ("Limiter detected. Stopping motor.")
    GPIO.output(gpioForward, False)
    
    # Roll motor back so the limiter is not pressed when it starts up again
    GPIO.output(gpioBackward, True)
    time.sleep(rollbackTimer)
    GPIO.output(gpioBackward, False)
    
    
    
    print ("Going backward until limiter detection in 5 seconds...")
    time.sleep(sleepTimer)
    GPIO.output(gpioBackward, True)
    while GPIO.input(gpioLimiter):
        print ("No limiter detected")
    
    print ("Limiter detected. Stopping motor.")
    GPIO.output(gpioBackward, False)
    
    
    # Roll motor forward to decompress the limiter
    GPIO.output(gpioForward, True)
    time.sleep(rollbackTimer)
    GPIO.output(gpioForward, False)
    
finally:
    # Cleanup
    GPIO.cleanup()
    print ("Test Complete. Goodbye!")


