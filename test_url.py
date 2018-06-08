





import requests
import json
import urllib



CARS_URL              = "https://www.reservauto.net/WCF/LSI/LSIBookingService.asmx/GetVehicleProposals?Callback=jQuery&CustomerID=%22%22&Longitude=0&Latitude=0&"
#LOGIN_URL             = "https://www.reservauto.net/Scripts/Client/Default.asp?BranchID=1&CurrentLanguageID=2&Username=%s&Password=%s&action=SIGN+IN"
LOGIN_URL             = "https://www.reservauto.net/Scripts/Client/Ajax/Mobile/Login.asp?callback=jQuery&BranchID=1&Username=%s&Password=%s&RememberMe=true&_="
LIST_RESERVATIONS_URL = 'https://www.reservauto.net/WCF/LSI/LSIBookingService.asmx/GetCurrentBooking?Callback=jQuery&CustomerID="C000029948"'
RESERVE_URL           = 'https://www.reservauto.net/WCF/LSI/LSIBookingService.asmx/CreateBooking?Callback=jQuery&CustomerID=""&VehicleID="%s"'



CANCEL_URL            = 'https://www.reservauto.net/WCF/LSI/LSIBookingService.asmx/CancelBooking?Callback=jQuery&CustomerID=""&VehicleID="%s"'




username = "79752"
password = 'giapantamazi'
session = requests.Session()


s = session.get(LOGIN_URL % (username, password))
print s.text

if s.status_code == 200:
    if "88522" in s.text:
        print "\n[+] Login Successful Nas"
    elif "Zanos" in s.text:
        print "\n[+] Login Successful Zanos"
    else:
        print "[-] Login failed"



s = session.get(LIST_RESERVATIONS_URL)
if s.status_code == 200:
    print s.text
    data_json = s.text[s.text.index("(") + 1: s.text.rindex(")")]
    data_json = json.loads(data_json)



carID = "JTDKDTB38E1068912"
s = session.get(RESERVE_URL % carID)
#print dir(s.request)
#print s.status_code



