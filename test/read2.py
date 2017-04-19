import smbus
import time
# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	#number = bus.read_byte(address)
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

while True:
	var = input("Enter 1 - 9: ")
	
	print "de barcode is %s" % getBarcode() 
	
	if not var:
		continue

	writeNumber(var)
	print "RPI: Hi Arduino, I sent you ", var
	# sleep one second
	time.sleep(1)
	
	number = readNumber()
	print "Arduino: Hey RPI, I received a digit ", number
