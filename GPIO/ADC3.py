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
light_adc = 1       # ADC
pot_adc = 0         # ADC
statusLED = 23
green = 25                          # Makes the LCD Green
light_Average = []                  # Average list used by the movavg function
l = 0                               # display  value for the light sensor
pot_Average = []                    # Average list used by the movavg function
p = 0                               # display value for the pot
rate = .1                           # The delay between refreshes + .125 seconds
bounce = 400
color = lcd.ON
print "Press CTRL+C to exit"

GPIO.setup(green, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(statusLED, GPIO.OUT)

lcd.backlight(color)
lcd.clear()


def analogRead(port):
    """
    Read the given ADC port and preform the necessary shifting of bits
    """
    spi.open(0, 0)
    if (port > 7) or (port < 0):
        print 'analogRead -- Port Error, Must use a port between 0 and 7'
        return -1
    r = spi.xfer2([1, (8 + port) << 4, 0])
    value = ((r[1] & 3) << 8) + r[2]
    spi.close()
    return value


def movavg(ave_list, length, value):
    """
    A function that smooths the results by averaging a list
    """
    ave_list.append(value)
    if length < len(ave_list):
        del ave_list[0]
    value = sum(ave_list)
    return value / len(ave_list)


def colorChange(channel):
    global color
    if channel == green:
        if color == lcd.ON:
            color = lcd.GREEN
        elif color == lcd.GREEN:
            color = lcd.OFF
        else:
            color = lcd.ON
    for i in range(3):
        lcd.backlight(color)
        sleep(.01)
    sleep(bounce/1000)


try:
    GPIO.add_event_detect(green, GPIO.RISING, callback=colorChange, bouncetime=bounce)

    while True:
        GPIO.output(statusLED, True)                                # Status Led On
        l = movavg(light_Average, 4, analogRead(light_adc))         # Read the light sensor and calculate the average
        lcd.home()                                                  # Tell the LCD to go back to the first character
        lcd.message('Pot: ' + str(analogRead(pot_adc)) + '         \nLight: ' + str(l) + '       ')  # Print info
        GPIO.output(statusLED, False)                               # Status Led Off
        sleep(rate)                                                 # Wait a little

except KeyboardInterrupt:
    GPIO.output(statusLED, False)
    spi.close()

finally:
    lcd.clear()
    lcd.backlight(lcd.OFF)
    GPIO.cleanup()