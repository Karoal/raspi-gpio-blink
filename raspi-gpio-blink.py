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

while True:
    gpio.output(11, 1 if counter % 2 == 0 else 0)
    gpio.output(13, 1 if counter % 4 == 0 else 0)
    gpio.output(15, 1 if counter % 8 == 0 else 0)
    time.sleep(delay)

    if counter >=  7:
        counter = 0
    else:
        counter += 1

