# 25.01.14
# Makes 3 LEDs blink using transistors and 3 GPIO outputs

import RPi.GPIO as gpio
import time
import datetime

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

counter = 0             # LEDs turn on/off based on whether counter is a multiple of a certain num
hour, minute = 7, 45    # time at which LEDs toggle fastest


def calc_time(hour, minute):
    """ Returns the appropriate delay for time.sleep """
    now = datetime.datetime.now()
    if now.hour < hour or now.hour == hour and now.minute < minute:
        waketime = datetime.datetime(now.year, now.month, now.day, hour, minute)
        delta = waketime - now
        return (delta.seconds / 86400 if delta.seconds > 600 else 0.00694)
    else:
        waketime = datetime.datetime(now.year, now.month, now.day, hour, minute) + datetime.timedelta(days=1)
        delta = waketime - now
        return (delta.seconds / 86400 if delta.seconds > 600 else 0.00694)

delay = calc_time(hour, minute)

while True:
    gpio.output(11, 1 if counter == 0 else 0)
    gpio.output(13, 1 if counter == 1 or counter == 3 else 0)
    gpio.output(15, 1 if counter == 2 else 0)
    time.sleep(delay)

    if counter >= 3:
        counter = 0
        delay = calc_time(hour, minute)
        print("sec: {0:20} per min: {1}".format(delay, 60 / delay))
    else:
        counter += 1
