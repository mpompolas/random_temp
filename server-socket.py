import socket
import json
import StringIO
import sys
import time


port = 12345


try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    print host

    sock.bind(("127.0.0.1", port))
    sock.listen(10)
except:
    print 'Trying again'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("127.0.0.1", port))
        sock.listen(10)
    except IOError as e:
        the_error = str(sys.exc_info()[1])
        if 'Errno 10013' in the_error:
            print 'The server is already running'
            time.sleep(2)

client, ip = sock.accept()
print ip

i = 1
while i<20:
    try:
        gpsdata = client.recv(2056)
        gpsdata = StringIO.StringIO(gpsdata)
        lines = gpsdata.readlines()
        print (str(lines) + ' The lines')

    except IOError as e:
        the_error = str(sys.exc_info()[1])
        print the_error
        if 'Errno 54' in the_error:
                print 'Restarting'
                time.sleep(2)
        if 'Errno 10013' in the_error:
            print 'The server is already running'
            time.sleep(2)
    i = i + 1

print 'Received and finished'
