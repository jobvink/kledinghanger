import smbus
import time
import RPi.GPIO as gpio
import thread

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

# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
# address = 0x04

# locaties op het rek
rack = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}

sizes = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}


def updater():
    while True:
        hangers_on_rack = get_hangers()
        for i in range(len(rack)):
            if hangers_on_rack[i]:
                rack[i] = get_barcode(i)
        time.sleep(2)


def set_led_color(color, address):
    if color == 'paars':
        write_number(30, address)
    elif color == 'geel':
        write_number(31, address)
    elif color == 'groen':
        write_number(32, address)
    elif color == 'oranje':
        write_number(33, address)
    elif color == 'blauw':
        write_number(34, address)


def write_number(value, address):
    try:
        bus.write_byte(address, value)
    except:
        pass


def get_hangers():
    hangers_on_rack = []
    for i in range(6):
        try:
            bus.read_byte(i)
            hangers_on_rack.append(True)
        except:
            hangers_on_rack.append(False)
    return hangers_on_rack


def read_number(address):
    # number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    for i in range(13):
        write_number(i, address)
        time.sleep(0.1)
        print chr(bus.read_byte(address))

    return 0


def get_barcode(address):
    barcode = ""
    for i in range(13):
        write_number(i, address)
        time.sleep(0.01)
        barcode += chr(bus.read_byte(address))
    return barcode


def reset_hanger():
    for i in range(6):
        write_number(40, i)

try:
    thread.start_new_thread(updater, ())
except:
    print 'Kon de updater thread niet starten'

updater()

while True:
    var = 5  # input("Enter 1 - 9: ")

    if not gpio.input(pin1):
        set_led_color('paars', 4)
        print 'paars'
    elif not gpio.input(pin2):
        set_led_color('geel', 4)
        print 'geel'
    elif not gpio.input(pin3):
        set_led_color('groen', 4)
        print 'groen'
    elif not gpio.input(pin4):
        set_led_color('oranje', 4)
        print 'oranje'
    elif not gpio.input(pin5):
        set_led_color('blauw', 4)
        print 'blauw'
