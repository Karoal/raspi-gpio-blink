# Test to see if 8 LEDs work

import RPi.GPIO as gpio
import time

pins = (7, 11, 12, 13, 15, 16, 18, 22)

gpio.setmode(gpio.BOARD)
gpio.setup( 7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)

for pin in pins:
    gpio.output(pin, 1)
    time.sleep(0.5)
