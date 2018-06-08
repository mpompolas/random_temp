


import datetime
import time


book_now =False
book_hour = 17
book_minute = 7


now = datetime.datetime.now()
hour = now.hour
minute = now.minute

if book_now:
    book_hour = hour
    book_minute = minute
    print 'booked'

elif not book_now:
    if book_minute < 10:
        text = ["\nThe time is set for:  " + str(book_hour) + ":0" + str(book_minute)]
    elif book_minute >= 10:
        text = "\nThe time is set for:  " + str(book_hour) + ":" + str(book_minute)
    print text
    while not (hour == book_hour and minute == book_minute):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        print 'waiting'
        time.sleep(15)

    print 'DONE'
