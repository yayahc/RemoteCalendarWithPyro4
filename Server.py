# Serveur
# @author : yayahc
# @version : 1.0

import Pyro4
import datetime
import time

@Pyro4.expose
class CalendrierDistant(object):
    def getAnnee(self):
        return datetime.datetime.now().year

    def getMois(self):
        return datetime.datetime.now().month

    def getJour(self):
        return datetime.datetime.now().day

daemon = Pyro4.Daemon()
uri = daemon.register(CalendrierDistant)

print("Loading ...")
time.sleep(2)
print("URI =", uri)
daemon.requestLoop()