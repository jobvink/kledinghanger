import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

pin0 = 26
pin1 = 19
pin2 = 13
pin3 = 6
pin4 = 5

# zorgt ervoor dat de gpio pinnen het knopje uit kunnen lezen
# het interne pull up register wordt gebruikt zodat
# er geen weerstandje tussen het knopje en de raspberry pi hoeft.
gpio.setup(pin0, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin3, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin4, gpio.IN, pull_up_down=gpio.PUD_UP)

def my_callback(channal):
    print channal
    print 'test'

gpio.add_event_detect(pin0, gpio.FALLING, callback=my_callback, bouncetime=300)

while True:
    pass
