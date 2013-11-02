#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

from time import sleep
import spidev
import RPi.GPIO as GPIO
from lib.Char_Plate.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import smbus

GPIO.setmode(GPIO.BCM)
lcd = Adafruit_CharLCDPlate(busnum=0)
spi = spidev.SpiDev()
pot_adc = 0         # ADC
l = []              # List for Light Sensor Averaging
statusLED = 23
print "Press CTRL+C to exit"
GPIO.setup(statusLED, GPIO.OUT)
lcd.backlight(lcd.ON)
lcd.clear()


def analogRead(port):
    """Read the given ADC port and preform the necessary shifting of bits"""
    spi.open(0, 0)
    if (port > 7) or (port < 0):
        print 'analogRead -- Port Error, Must use a port between 0 and 7'
        return -1
    r = spi.xfer2([1, (8 + port) << 4, 0])
    value = ((r[1] & 3) << 8) + r[2]
    spi.close()
    return value


def movavg(ave_list, length, value):
    """A function that smooths the results by averaging a list"""
    ave_list.append(value)
    if length < len(ave_list):
        del ave_list[0]
    value = 0
    for x in ave_list[:]:
        value += x
    return value / len(ave_list)

try:
    while True:
        # Change the Back-light based on what button has been pressed
        if lcd.buttonPressed(lcd.DOWN):
            lcd.backlight(lcd.ON)
        if lcd.buttonPressed(lcd.UP):
            lcd.backlight(lcd.OFF)
        lcd.home()                                                  # Tell the LCD to go back to the first character
        GPIO.output(statusLED, True)                                # Status Led On
        lcd.message('Potentiometer:\n' + str(
            movavg(l, 4, analogRead(pot_adc))) + '     ')           # Read analog value and send it to the display
        sleep(.1)                                                   # Wait a little
        GPIO.output(statusLED, False)                               # Status Led off
        sleep(.155)                                                 # Wait a bit longer

except KeyboardInterrupt:
    GPIO.output(statusLED, False)
    spi.close()

finally:
    lcd.clear()
    lcd.backlight(lcd.OFF)
    GPIO.cleanup()