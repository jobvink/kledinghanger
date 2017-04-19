import smbus
import time
import RPi.GPIO as gpio
import thread
import requests
import json

# zet het board op de goede modus om de knopjes op te vangen
gpio.setmode(gpio.BCM)

# deze varialblen geven aan welke host en poort het script moet gebruiken
host = "192.168.178.106"
port = "8000"

# zet variablen voor de knopjes
pin1 = 26
pin2 = 19
pin3 = 13
pin4 = 6
pin5 = 5

# zorgt ervoor dat de gpio pinnen het knopje uit kunnen lezen
# het interne pull up register wordt gebruikt zodat
# er geen weerstandje tussen het knopje en de raspberry pi hoeft.
gpio.setup(pin1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin3, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin4, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(pin5, gpio.IN, pull_up_down=gpio.PUD_UP)

# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# locaties op het rek
rack = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}

# verbind de locaties op het rek met een maat
sizes = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}

# deze demon is verantwoordelijk voor
# het up to date houden van de barcodes op het rek
# en de bijbehoordende maten
def statistics_demon():
    while True:
        # rack updater
        print rack
        hangers_on_rack = get_hangers()
        for i, value in rack.iteritems():
            if hangers_on_rack[i]:
                if hanger_has_clothin(i) == 1:
                    barcode = get_barcode(i)
                    if rack[i] == barcode:
                        continue
                    else:
                        rack[i] = barcode
                        print 'barcode: %s gevonden op hanger %i' % (rack[i], i)
                        data = {
                            'rack': 1,
                            'barcode': barcode
                        }
                        requests.post('http://%s:%s/rack/update' % (host, port), data=json.dumps(data))
                        print '%s verstuurd naar server' % barcode
                        try:
                            response = requests.get('http://%s:%s/products/%s' % (host, port, barcode))
                            response = response.json()
                            sizes[i] = response['size']
                            print 'informatie gevonden over %s: ' %rack[i]
                        except:
                            print 'geen informatie over %s' % rack[i]
                else:
                    if rack[i] is None:
                        pass
                    else:
                        barcode = rack[i]
                        data = {
                            'rack': 1,
                            'barcode': barcode
                        }
                        requests.post('http://%s:%s/rack/destroy' % (host, port), data=json.dumps(data))
                        print '%s verwijderd van server' % barcode
                        rack[i] = None
                        sizes[i] = None
            else:
                if value is not None:
                    rack[i] = None
                    sizes[i] = None

        # deze regels zorgt ervoor dat de database up-to-date blijft
        # update_rack_entrys()

        time.sleep(1)


# deze functie zorgt er voor dat de entrys in de database geupdate worden
# def update_rack_entrys():
#     for i in changed:
#         barcode = rack[i]
#         if barcode:
#             data = {
#                 'rack': 1,
#                 'barcode': barcode
#             }
#             requests.post('http://%s:%s/rack/update' % (host, port), data=json.dumps(data))
#             changed.remove(i)
#             print '%s verstuurd naar server' % barcode
#         else:
#             data = {
#                 'rack_id': 1,
#                 'barcode': barcode
#             }
#             requests.post('http://%s:%s/rack/destroy' % (host, port), data=json.dumps(data))
#             changed.remove(i)
#             print '%s verwijderd van server' % barcode


# een demon voor test doeleinden
def test_demon():
    while True:
        print sizes


# deze functie zorgt er voor dat een ledje op de hanger oplicht
# in een bepaalde kleur
# de eerste parameter color geeft de te zetten kleur aan,
# de tweede parameter address specificeert op welke hanger die kleur moet branden
# de nummers die de raspberry pi verstuurd worden opgenvangen door een arduino,
# deze arduino zorgt er vervolgens voor dat het ledje met de goede kleur oplicht.
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


# deze functie verstuurd een nummer naar een gespecificeerd adres.
def write_number(value, address):
    try:
        bus.write_byte(address, value)
    except:
        pass


# deze functie geeft een array met alle adressen van de hangers die op het reck hangen.
def get_hangers():
    hangers_on_rack = []
    for i in range(6):
        try:
            bus.read_byte(i)
            hangers_on_rack.append(True)
        except:
            hangers_on_rack.append(False)
    return hangers_on_rack


# deze functie geeft het response van de arduino terug
def read_response(address):
    try:
        return bus.read_byte(address)
    except:
        print "kon het antwoord niet lezen"
        return None


# deze functie geeft de barcode van een gespecificeerd adres terug.
def get_barcode(address):
    barcode = ""
    for i in range(13):
        write_number(i, address)
        time.sleep(0.01)
        try:
            barcode += chr(bus.read_byte(address))
        except:
            barcode = None
    return barcode


# deze functie reset alle hangers door code 40 naar de hangers te sturen.
def reset_hangers():
    for i in range(6):
        try:
            write_number(40, i)
        except:
            pass


# deze functie geeft de positie van een gespecificeerde maat terug
# de parameter size moet een maat XS, S, M, L of XL ontvangen
# de maten zijn in hoofdletters en hoofdletter gevoelig
def get_positions_of_sizes(size):
    address_by_size = []
    for address, s in sizes.iteritems():
        if s == size:
            address_by_size.append(address)
    return address_by_size


# deze functie stuurt code 50 naar de hanger
# het antwoord van de hanger is:
# 1 als het kledingstuk gepast is.
# 0 als het kledingstuk niet gepast is.
def get_tried(address):
    write_number(50, address)
    return read_response(address)


def hanger_has_clothin(address):
    write_number(60, address)
    return read_response(address)


# deze functie zorgt er voor dat alle hangers met de gespecificeerde maat oplichten
# de parameter size moet een maat XS, S, M, L of XL ontvangen
def set_hanger_color(size):
    addresses = get_positions_of_sizes(size)
    if size == 'XS':
        for s in addresses:
            set_led_color('paars', s)
            print 'hanger %i heeft maat XS' % s
    elif size == 'S':
        for s in addresses:
            set_led_color('geel', s)
            print 'hanger %i heeft maat S' % s
    elif size == 'M':
        for s in addresses:
            set_led_color('groen', s)
            print 'hanger %i heeft maat M' % s
    elif size == 'L':
        for s in addresses:
            set_led_color('oranje', s)
            print 'hanger %i heeft maat L' % s
    elif size == 'XL':
        for s in addresses:
            set_led_color('blauw', s)
            print 'hanger %i heeft maat XL' % s


# deze regels starten de demon op die voor het up-to-date houden
# van de barcodes en bijbehoorende maten zorgen.
try:
    thread.start_new_thread(statistics_demon, ())
except:
    print "kon de statistics demon niet starten."

# deze loop zorgt er voor dat de knopjes opgevangen worden
# en dat de juiste kleur op de hanger oplicht
while True:
    if not gpio.input(pin1):  # pin voor maat S
        set_hanger_color('XS')
    elif not gpio.input(pin2):
        set_hanger_color('S')
    elif not gpio.input(pin3):
        set_hanger_color('M')
    elif not gpio.input(pin4):
        set_hanger_color('L')
    elif not gpio.input(pin5):
        set_hanger_color('XL')
