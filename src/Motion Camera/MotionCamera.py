#!/usr/bin/env python3

from picamera import PiCamera
import RPi.GPIO as GPIO
import time

# Create Camera Instance
camera = PiCamera()

pirPin = 17    # the pir connected to pin17
ledPin = 27    # the led connected to pin17




def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pirPin, GPIO.IN)
    GPIO.setup(ledPin, GPIO.OUT)
    camera.start_preview(alpha=200)

def main():
    i = 1
    while True:
        pirVal = GPIO.input(pirPin)
        
        # Turn on light and capture picture if motion is detected
        if pirVal==GPIO.HIGH:
            GPIO.output(ledPin, GPIO.HIGH)
            camera.capture('/home/pi/security_camera/capture%s.jpg' % i)
            print('The number is %s' % i)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(3)
            i = i + 1
        else:
            print('no motion')
            time.sleep(1)

def destroy():
    GPIO.cleanup()
    camera.stop_preview()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
