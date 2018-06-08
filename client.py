# Client side

import socket
import time
import sys

port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("127.0.0.1", port)) #connecting to pi as client 5 seconds
except IOError as e:
    the_error = str(sys.exc_info()[1])
    print the_error
    if 'Errno 10061' in the_error:
        print 'Server Down'
        time.sleep(2)
        raise
i = 1
while True:
    i = i+1
    try:
        s.send(str(i) + '\n' + str(i) + '\n') #send to server
        print 'Coordinates sent'
        time.sleep(0.2) #wait for 5 seconds
    except IOError as e:
        print 'Connection reset by peer'
        time.sleep(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", port))
        except IOError as e:
            the_error = str(sys.exc_info()[1])
            print the_error
            if 'Errno 10061' in the_error:
                print 'Server Down'
                time.sleep(2)
                raise


    
