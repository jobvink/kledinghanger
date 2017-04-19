pin0 = 'test'
pin1 = 'test'
for i in range(2):
    pin = None
    exec ("pin = pin%i" % i)
    print pin