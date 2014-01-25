import RPi.GPIO as gpio
import time

#Makes 3 LEDs blink using transistors and 3 GPIO outputs

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

counter = 0             # LEDs turn on/off based on whether counter is a multiple of a certain num
delay = 60/(2*128)      # argument for time.sleep, delay between each while loop
toggle = {11: False,   # bool values for toggling
          13: False,
          15: False}

while True:
    toggle[11] = not toggle[11]
    gpio.output(11, toggle[11])

    if counter % 2 == 0:
        toggle[13] = not toggle[13]
        gpio.output(13, toggle[13])

    if counter % 4 == 0:
        toggle[15] = not toggle[15]
        gpio.output(15, toggle[15])

    time.sleep(delay)
    counter += 1
