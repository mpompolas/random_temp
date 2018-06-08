import androidhelper
import time
import geocoder
import warnings
warnings.filterwarnings("ignore")

droid = androidhelper.Android ()

'''
droid.startLocating()
time.sleep(0.0003)
loc = droid.readLocation().result
all = droid.readLocation()

droid.stopLocating()

a =droid.checkRingerSilentMode()

#print a.result
print loc
'''

g = geocoder.google ([45.523240, -73.553739], method='reverse')

print g.city.encode ('utf-8')

city = g.city.encode ('utf-8')
number = str(g.housenumber.encode ('utf-8'))
address = str(g.street.encode ('utf-8'))

droid.notify(number + ' ' + address, 'Type: ')





