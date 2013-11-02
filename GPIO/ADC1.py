#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

import time
import spidev
import RPi.GPIO as GPIO

# This program reads an analogue value form a potentiometer attached to port 0 on the MCP3008 Chip

spi = spidev.SpiDev()
pot_adc = 0
statusLED = 23          # GPIO port that our Status led is connected to

GPIO.setmode(GPIO.BCM)
GPIO.setup(statusLED, GPIO.OUT)

print "Press CTRL+C to exit"


def analogRead(port, bus=0, ce=0):
    """Read the given ADC port and preform the necessary shifting of bits"""
    spi.open(bus, ce)      # CE port that the MCP3008 is connected to
    if (port > 7) or (port < 0):
        print 'analogRead -- Port Error, Must use a port between 0 and 7'
        return -1
    r = spi.xfer2([1, (8 + port) << 4, 0])
    value = ((r[1] & 3) << 8) + r[2]
    spi.close()
    return value

try:
    while True:
        GPIO.output(statusLED, True)   # Status Led On
        print analogRead(pot_adc)    # Print read value
        time.sleep(.125)               # Wait a little
        GPIO.output(statusLED, False)  # Status Led Off
        time.sleep(.175)               # Wait a bit longer

except KeyboardInterrupt:
    GPIO.output(statusLED, False)

finally:
    GPIO.cleanup()