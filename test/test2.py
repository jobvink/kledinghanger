import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

pin1 = 26
pin2 = 19
pin3 = 13
pin4 = 6
pin5 = 5

gpio.setup(pin1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin3, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin4, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin5, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
    if not gpio.input(pin2):
        print('Button Pressed')
        time.sleep(0.2)