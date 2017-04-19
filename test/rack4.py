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
key = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjhiOWQxNTZkYTY0MDU4OTM1MzVjYzA5NmVkY2Q1YWQ3OTkzOGMwYzJjODM3MWNhMTdhYzdkNmJlN2U5ZTg3ODFiNDljMzUxZmMxY2I0NTNmIn0.eyJhdWQiOiI2IiwianRpIjoiOGI5ZDE1NmRhNjQwNTg5MzUzNWNjMDk2ZWRjZDVhZDc5OTM4YzBjMmM4MzcxY2ExN2FjN2Q2YmU3ZTllODc4MWI0OWMzNTFmYzFjYjQ1M2YiLCJpYXQiOjE0OTIyNjYwNTYsIm5iZiI6MTQ5MjI2NjA1NiwiZXhwIjoxNTIzODAyMDU2LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.jRErPZ7rtC51Y-qejzHoyjayN7Ek9n4B7825G-PIrr_BU35cdh8TgKKDTF4Kj_NAJRTuu_bAj7p0ov13rDIWNbUG33zGs0r8iXkXGTKgHbWZWWQjZRK5wnMKfOJMMUw7q_C1vDNmVeE0ToS94gP1OH-9G5MD9Vy8aDQSWKRKEX7CDQPOm3yWV5SNNn89qkvLcNHhzvLv2fBhkpLRxXfhaPycnTj2JY0LCZ7N0Km_rNcQh038LOwVXZ-hHnvFhER5JemR3JPuLoXBqsLjKSq2zrYFe95B77HxOK3B2y19P1EYmTlxvDsAJiqn99tIveyCk68pp_SbIhZeH_Kpdb_m0FE_tu2fAUr8oXbXwJ0CglXaly3hV955XHw2Ib-22SEcUVydEficUHaVWyFXBRGWQbdU44qoRHUeMVF8AwxlFAk9MS7SQ4fws_fKg8kJspRCYkkIklOyVpiTg_ZKWH92lF6f249tAvZRE3ekm-2Lwrijcj_xGDtKmhrv5rEQKn6N83MybsqP-hq6Jad-ORO_QFLJzpE9JYaYYuK6gtaiHfRmf3dWhBXNzK4-IEubnxEpTNi96ryFuPkrZnF30QGEHvLDPbr3PGYzD-hMAooutb08x2gyb2I08eMQYC4TRVB6YNwtevscA_xpmzlV-UcLaDcjA5iAUnnSZ5ZW5uKKQWQ'}

# array met alle maten die het systeem aan kan
system_sizes = ['128', '140', '152', '164', '176']
# kleur bij maat
size_color = {
    '128': 'paars',
    '140': 'geel',
    '152': 'groen',
    '164': 'oranje',
    '176': 'blauw'
}

# zet variablen voor de knopjes
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
                if hanger_has_clothing(i) == 1:
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
                        requests.post('http://%s:%s/api/rack/attach' % (host, port), data=json.dumps(data), headers=key)
                        print '%s verstuurd naar server' % barcode
                        try:
                            response = requests.get('http://%s:%s/api/products/%s' % (host, port, barcode), headers=key)
                            try:
                                if response.json()['status'] == 'faild':
                                    print '%s niet in database' % barcode
                                    break
                            except KeyError:
                                pass
                            response = response.json()
                            sizes[i] = response['size']
                            print 'informatie gevonden over %s: ' % rack[i]
                        except requests.ConnectionError:
                            print 'geen verbinding met server'
                else:
                    if rack[i] is None:
                        pass
                    else:
                        barcode = rack[i]
                        data = {
                            'rack': 1,
                            'barcode': barcode
                        }
                        requests.post('http://%s:%s/api/rack/detach' % (host, port), data=json.dumps(data), headers=key)
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


# een demon voor test doeleinden
def test_demon():
    while True:
        print sizes


def set_led_color(color, address):
    """
    deze functie zorgt er voor dat een ledje op de hanger oplicht
    in een bepaalde kleur
    de nummers die de raspberry pi verstuurd worden opgenvangen door een arduino,
    deze arduino zorgt er vervolgens voor dat het ledje met de goede kleur oplicht.
    :param color: geeft de te zetten kleur aan,
    :param address: specificeert op welke hanger die kleur moet branden
    """
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
    """
    deze functie verstuurd een nummer naar een gespecificeerd adres.
    :param value:
    :param address:
    """
    try:
        bus.write_byte(address, value)
    except IOError:
        pass


def get_hangers():
    """
    deze functie geeft een array met alle adressen van de hangers die op het reck hangen.
    :return:
    """
    hangers_on_rack = []
    for i in range(6):
        try:
            bus.read_byte(i)
            hangers_on_rack.append(True)
        except IOError:
            hangers_on_rack.append(False)
    return hangers_on_rack


def read_response(address):
    """
    deze functie geeft het response van de arduino terug
    :param address:
    :return:
    """
    try:
        return bus.read_byte(address)
    except IOError:
        print "kon het antwoord niet lezen"
        return None


def get_barcode(address):
    """
    deze functie geeft de barcode van een gespecificeerd adres terug.
    :param address:
    :return:
    """
    barcode = ""
    for i in range(13):
        write_number(i, address)
        time.sleep(0.01)
        try:
            barcode += chr(bus.read_byte(address))
        except IOError:
            barcode = None
    return barcode


def reset_hangers():
    """
    deze functie reset alle hangers door code 40 naar de hangers te sturen.
    """
    for i in range(6):
        write_number(40, 1)


def get_positions_of_sizes(size):
    """
    deze functie geeft de positie van een gespecificeerde maat terug
    :param size: ontvangt een maat in de array system_sizes
    :return: Array van alle adressen met bijbehoorende maat
    """
    address_by_size = []
    for address, s in sizes.iteritems():
        if s == size:
            address_by_size.append(address)
    return address_by_size


def get_tried(address):
    """
    deze functie stuurt code 50 naar de hanger
    het antwoord van de hanger is:
    :param address: het adres van de hanger
    :return: 1 als het kledingstuk gepast is. 0 als het kledingstuk niet gepast is.
    """
    write_number(50, address)
    return read_response(address)


def hanger_has_clothing(address):
    """
    deze funcie kijkt of er een kleding op de hanger zit
    :param address: Het address van de hanger
    :return:
    """
    write_number(60, address)
    return read_response(address)


def set_hanger_color(size):
    """
    deze functie zorgt er voor dat alle hangers met de gespecificeerde maat oplichten
    :param size: ontvangt een maat in de array system_sizes
    """
    addresses = get_positions_of_sizes(size)
    for system_size in system_sizes:
        if size == system_size:
            for address in addresses:
                set_led_color(size_color[size], address)
                print 'hanger %i heeft maat %s' % (address, size_color['size'])


# deze regels starten de demon op die voor het up-to-date houden
# van de barcodes en bijbehoorende maten zorgen.
try:
    thread.start_new_thread(statistics_demon, ())
except thread.error:
    print "kon de statistics demon niet starten."


def main():
    # deze loop zorgt er voor dat de knopjes opgevangen worden
    # en dat de juiste kleur op de hanger oplicht
    while True:
        for i in range(len(system_sizes)):
            pin = None
            exec ("pin = pin%i" % i)
            if gpio.input(pin):
                set_hanger_color(system_sizes[i])
                # test
                print 'Knop voor maat %s ingedrukt' % system_sizes[i]


if __name__ == '__main__':
    main()
