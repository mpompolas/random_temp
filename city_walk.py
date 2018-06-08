import androidhelper
import time
import geocoder
import warnings
warnings.filterwarnings("ignore")

droid = androidhelper.Android()

print '\n\n'

while True:

    droid.startLocating()
    time.sleep(5)
    loc = droid.readLocation().result
    droid.stopLocating()

    try:
        latitude = loc['gps']['latitude']
        longitude = loc['gps']['longitude']

        g = geocoder.google([latitude, longitude], method='reverse')

        if g.housenumber is not None and g.street is not None:
            number = str(g.housenumber.encode('utf-8'))
            address = str(g.street.encode('utf-8'))
            print(number + ' ' + address)

        elif g.housenumber is None and g.street is not None:
            print address

    except:
        time.sleep(2)



