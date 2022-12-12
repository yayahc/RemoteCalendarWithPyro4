# Serveur who get RemoteCalendar Objet
# @author : yayahc
# @version : 2.0

import Pyro4
import datetime
import time
from RemoteCalendar import RemoteCalendarClass

try:
	daemon = Pyro4.Daemon()
	uri = daemon.register(RemoteCalendarClass)
	print("succes")
except:
	print("error")

print("Loading ...")
time.sleep(2)
print("URI =", uri)
daemon.requestLoop()
