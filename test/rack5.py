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
port = "8002"
key = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjAxZTczMTQ2NWQwNGNjNGIyOTczNDkwZDBmOTc2NmE1NWI1YmQxMDdjYTFkMDU4MDczN2Q2OWIwMmU4ZTIyNjc1YWE1NTkzYTZmNjViYzY1In0.eyJhdWQiOiIyIiwianRpIjoiMDFlNzMxNDY1ZDA0Y2M0YjI5NzM0OTBkMGY5NzY2YTU1YjViZDEwN2NhMWQwNTgwNzM3ZDY5YjAyZThlMjI2NzVhYTU1OTNhNmY2NWJjNjUiLCJpYXQiOjE0OTI4NTk3MDAsIm5iZiI6MTQ5Mjg1OTcwMCwiZXhwIjoxNTI0Mzk1NzAwLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.ynJNQHoC5Y6DYDmUfovo05gx4lTXJd61zrnuu1NHs4dykRH2jkLCoolLwHz-ubmFIINn5YZCOjaqqxQxFfWpBMNU1hSqfgomLPeW059SYb4_T6Hj-XtZgFfaOjKoYEwa0hWJI8kUaRtxK0TxPAhMTY02ENJd9D9m56_9WVfcp-av5FXe8RTYbEL2lni9-JAqc6ps6URfpslS5R53DKujDY0SPIu2rmdUvYLB-c_lLNdTjV-cMunp4eiNWiMJtxmj8dQf0qriSfqgExoZpIkJnWkS_XUp6AEDfj8-0go5Fpb5ySfquIyXIDqhg45OMLJX1PJQmMtsJoPLZWiNNZXTMGRSlrfzPIxxXHlayxAlzRn7epPoN-n22KxIFVwES8KJKnxlDhdVm6KdHQ10tg4RBTpaUkJZ6mUnGTFiQedQ9FwCceOkpsXfkK9eG8pk_ZXm31PPUVFcwbNMzM3-Qvugf8saSl05nROj-877bCf_8QInKTVVqcoqIKJOC0JgxukJBq_nUOhhsO2xa6Az68sUXOPcUwbv4zd7B_afAlIHD72xVa3mHRCtqz3BDYkkeCz9FwvT-IxBeehm2MdaOvesDzic5x-5oAqQUiKU3426EJ36y-S0kxRkyy01dUurnC2NOg8tk3u17kWjNU8M9JtmH7wdMLN9Zl0XKaIerI0RspE'}

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
pins = [26, 19, 13, 6, 5]

# zorgt ervoor dat de gpio pinnen het knopje uit kunnen lezen
# het interne pull up register wordt gebruikt zodat
# er geen weerstandje tussen het knopje en de raspberry pi hoeft.
for pin in pins:
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)

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
        try:
            print rack
            hangers_on_rack = get_hangers()
            for i, value in rack.iteritems():
                if hangers_on_rack[i]:
                    if hanger_has_clothing(i) == 1:
                        barcode = get_barcode(i)
                        if rack[i] == barcode:
                            continue
                        else:
                            attach_barcode(i, barcode)
                    elif hanger_has_clothing(i) == 0:
                        if rack[i] is None:
                            pass
                        else:
                            barcode = rack[i]
                            detach_barcode(barcode)
                            rack[i] = None
                            sizes[i] = None
                else:
                    if value is not None:
                        detach_barcode(rack[i])
                        rack[i] = None
                        sizes[i] = None
            time.sleep(1)
        except UnicodeDecodeError:
            print 'hanger verwijderd tijdens actie'


def attach_barcode(i, barcode):
    if barcode is None:
        return None
    rack[i] = barcode
    print 'barcode: %s gevonden op hanger %i' % (rack[i], i)
    data = {
        'rack': 1,
        'barcode': barcode
    }
    try:
        attach_response = requests.post('http://%s:%s/api/rack/attach' % (host, port), data=json.dumps(data),
                                        headers=key)
        print attach_response.json()['status']
    except requests.exceptions.ConnectionError:
        print 'Geen verbinding met de server'
    try:
        response = requests.get('http://%s:%s/api/products/%s' % (host, port, barcode), headers=key)
        try:
            if response.json()['status'] == 'faild':
                print '%s niet in database' % barcode
        except KeyError:
            pass
        except ValueError:
            print 'foute key'
        response = response.json()
        sizes[i] = response['size']
        print 'informatie gevonden over %s: ' % rack[i]
    except requests.ConnectionError:
        print 'geen verbinding met server'


def detach_barcode(barcode):
    data = {
        'rack': 1,
        'barcode': barcode
    }
    try:
        detach_response = requests.post('http://%s:%s/api/rack/detach' % (host, port), data=json.dumps(data),
                                        headers=key)
        print detach_response.json()['status']
    except requests.exceptions.ConnectionError:
        print 'Geen verbinding met server'


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
                print 'hanger %i heeft maat %s' % (address, size_color[size])


def knoppen(pressed_pin):
    set_hanger_color(system_sizes[pins.index(pressed_pin)])
    print 'Knop voor maat %s ingedrukt' % system_sizes[pins.index(pressed_pin)]


if __name__ == '__main__':
    # deze regels starten de demon op die voor het up-to-date houden
    # van de barcodes en bijbehoorende maten zorgen.
    # try:
    #     thread.start_new_thread(knoppen, ())
    # except thread.error:
    #     print "kon de statistics demon niet starten."
    for pin in pins:
        gpio.add_event_detect(pin, gpio.FALLING, callback=knoppen, bouncetime=300)

    statistics_demon()
