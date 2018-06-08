
import threading
import androidhelper


class CountThread(threading.Thread):
    def run(self):
        droid.view(url)
        print 'In the function'

droid = androidhelper.Android()

###############################################
lat = 45.514951
lon = -73.570179
destination_lat = 45.451862
destination_lon = -73.872942

first='http://maps.google.com/?daddr='
start='&saddr='
walk ='&dirflg=w'
zoom ='&sspn=0.001,0.001'
url = first + str(destination_lat) + ',' + str(destination_lon) + start + str(lat) + ',' + str(
    lon) + walk + zoom
###############################################


print 'About to enter'
a = CountThread()
print(dir(a))
a.start()

print 'Exit'






a = CountThread()
b = CountThread()
a.start()
b.start()