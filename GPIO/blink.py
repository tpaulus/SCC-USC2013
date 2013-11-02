#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#use the common numeration,
#also the one found on the Adafruit Cobbler

led = 21                    # GPIO Port to which the LED is connected
delay = .5
GPIO.setup(led, GPIO.OUT)   # Set 'led' as and Output

print "Press CTRL+C to exit"

try:
    while True:
        GPIO.output(led, True)   # led On
        sleep(delay)             # wait 'delay' seconds
        GPIO.output(led, False)  # led Off
        sleep(delay)             # wait another 'delay' seconds

except KeyboardInterrupt:
    GPIO.output(led, False)

finally:
    GPIO.cleanup()