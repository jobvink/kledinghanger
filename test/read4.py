import smbus
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setup(37, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(35, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(33, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(32, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(29, gpio.IN, pull_up_down=gpio.PUD_UP)

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


def readNumber():
    # number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    for i in range(13):
        writeNumber(i)
        time.sleep(0.1)
        print chr(bus.read_byte(address))

    return 0


def getBarcode():
    try:
        barcode = ""
        for i in range(13):
            writeNumber(i)
            time.sleep(0.01)
            barcode += chr(bus.read_byte(address))
        return barcode
    except:
        print 'read faild'

def resetHanger():
    writeNumber(40)


while True:
    var = input("Enter 1 - 9: ")

    if var == 1:
        print "de barcode is %s" % getBarcode()
    elif var == 2:
        for i in range(6):
            try:
                bus.read_byte(i)
                print "hanger %i wel op het rek" % i
            except:
                print "hanger %i niet op het rek" % i
    elif gpio.input(37):
        setLedColor('paars')
        print 'paars'
    elif gpio.input(35):
        setLedColor('geel')
        print 'geel'
    elif gpio.input(33):
        setLedColor('groen')
        print 'groen'
    elif gpio.input(31):
        setLedColor('oranje')
        print 'oranje'
    elif gpio.input(29):
        setLedColor('blauw')
        print 'blauw'
