# 25.01.14
# Makes 3 LEDs blink using transistors and 3 GPIO outputs

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

counter = 0             # LEDs turn on/off based on whether counter is a multiple of a certain num
delay = 60/(4*128)      # argument for time.sleep, delay between each while loop

hour, minute = 6, 45    # time at which LEDs toggle fastest

waketime = time.strptime(str(hour) + " " + str(minute), "%H %M")
print(waketime)


def calc_time(t):
    """ Returns the appropriate delay for time.sleep """
    return (time.mktime(t) % 3600*24) / 3600*12

while True:
    gpio.output(11, 1 if counter == 0 else 0)
    gpio.output(13, 1 if counter == 1 or counter == 3 else 0)
    gpio.output(15, 1 if counter == 2 else 0)
    time.sleep(delay)

    if counter >= 3:
        counter = 0
        delay = calc_time(waketime)
        print(delay)
    else:
        counter += 1
