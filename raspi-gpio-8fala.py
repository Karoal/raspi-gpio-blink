# 25.01.14
# Makes 3 LEDs blink using transistors and 3 GPIO outputs

import RPi.GPIO as gpio
import time
import datetime

pins = (22, 18, 16, 15, 13, 12, 11, 7)
gpio.setmode(gpio.BOARD)
for pin in pins:
    gpio.setup(pin, gpio.OUT)

counter = 0             # LEDs turn on/off based on whether counter is a multiple of a certain num
hour, minute = 7, 45    # time at which LEDs toggle fastest


def calc_time(hour, minute):
    """ Returns the appropriate delay for time.sleep """
    now = datetime.datetime.now()
    if now.hour < hour or now.hour == hour and now.minute < minute:
        waketime = datetime.datetime(now.year, now.month, now.day, hour, minute)
        delta = waketime - now
        return (delta.seconds / 57600 if delta.seconds > 600 else 0.01)
    else:
        waketime = datetime.datetime(now.year, now.month, now.day, hour, minute) + datetime.timedelta(days=1)
        delta = waketime - now
        return (delta.seconds / 57600 if delta.seconds > 600 else 0.01)

delay = calc_time(hour, minute)

while True:
    if counter <= 7:
        print("wee")
        for x in range(8):
            gpio.output(pins[x], 1 if counter == x else 0)
    if counter <= 15 and counter > 7:
        print("moo")
        for x in range(8):
            gpio.output(pins[x], 1 if (counter - 8) >= x else 0)
    if counter <= 23 and counter > 15:
        print("moo")
        for x in range(8):
            gpio.output(pins[x], 1 if (counter - 16) != x else 0)
    if counter <= 31 and counter > 23:
        print("moo")
        for x in range(8):
            gpio.output(pins[x], 1 if (counter - 24) < x else 0)

    if counter >= 31:
        counter = 0
        delay = calc_time(hour, minute)
    else: counter += 1
    time.sleep(delay)
