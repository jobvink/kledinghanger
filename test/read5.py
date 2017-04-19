import smbus
import time
import RPi.GPIO as gpio

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
address = 0x04

def setLedColor(color):
    if color == 'paars':
        writeNumber(30)
    elif color == 'geel':
        writeNumber(31)
    elif color == 'groen':
        writeNumber(32)
    elif color == 'oranje':
        writeNumber(33)
    elif color == 'blauw':
        writeNumber(34)


def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def getHangers():
    for i in range(6):
        try:
            bus.read_byte(i)
            print "hanger %i wel op het rek" % i
        except:
            print "hanger %i niet op het rek" % i


def readNumber():
    # number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    for i in range(13):
        writeNumber(i)
        time.sleep(0.1)
        print chr(bus.read_byte(address))

    return 0


def getBarcode():
    barcode = ""
    for i in range(13):
        writeNumber(i)
        time.sleep(0.01)
        barcode += chr(bus.read_byte(address))
    return barcode

def resetHanger():
    writeNumber(40)


while True:
    var = 5 #input("Enter 1 - 9: ")

    if var == 1:
        print "de barcode is %s" % getBarcode()
    elif var == 2:
        print "hangers:"
    elif not gpio.input(pin1):
        setLedColor('paars')
        print 'paars'
    elif not gpio.input(pin2):
        setLedColor('geel')
        print 'geel'
    elif not gpio.input(pin3):
        setLedColor('groen')
        print 'groen'
    elif not gpio.input(pin4):
        setLedColor('oranje')
        print 'oranje'
    elif not gpio.input(pin5):
        setLedColor('blauw')
        print 'blauw'
