import smbus
import time
import RPi.GPIO as gpio
import thread
import requests

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

def size_updater():
    while True:
        for i in range(1, 6):
            if rack[i]:
                print rack[i]
                response = requests.get('http://127.0.0.1:8000/products/%s' % rack[i]).json()
                sizes[i] = response['size']
        time.sleep(2)

def rack_updater():
    while True:
        hangers_on_rack = get_hangers()
        for i in range(len(rack)):
            if hangers_on_rack[i]:
                rack[i] = get_barcode(i)
        time.sleep(2)

def test_demon():
    while True:
        print sizes


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

def get_positions_of_sizes(size):
    address_by_size = []
    for address, s in sizes.iteritems():
        if s == size:
            address_by_size.append(address)
    return address_by_size

def set_hanger_color(maat):
    addresses = get_positions_of_sizes(maat)
    if maat == 'XS':
        for s in addresses:
            set_led_color('paars', s)
    elif maat == 'S':
        for s in addresses:
            set_led_color('geel', s)
    elif maat == 'M':
        for s in addresses:
            set_led_color('groen', s)
    elif maat == 'L':
        for s in addresses:
            set_led_color('oranje', s)
    elif maat == 'XL':
        for s in addresses:
            set_led_color('blauw', s)
try:
    thread.start_new_thread(rack_updater, ())
except:
    print 'Kon de rack updater thread niet starten'

try:
    thread.start_new_thread(size_updater, ())
except:
    print 'Kon de size updater thread niet starten'

thread.start_new_thread(test_demon, ())


while True:
    if not gpio.input(pin1): # pin voor maat S
        set_hanger_color('XS')
        print 'paars'
    elif not gpio.input(pin2):
        set_hanger_color('S')
        print 'geel'
    elif not gpio.input(pin3):
        set_hanger_color('M')
        print 'groen'
    elif not gpio.input(pin4):
        set_hanger_color('L')
        print 'oranje'
    elif not gpio.input(pin5):
        set_hanger_color('XL')
        print 'blauw'
