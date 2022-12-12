# Remote Calendar Class
# @author : yayahc
# @version : 2.0

import Pyro4
import datetime
from ICalendar import year, month, day


@Pyro4.expose
class RemoteCalendarClass(object):
    def getYear(self):
        return year()

    def getMonth(self):
        return month()

    def getDay(self):
        return day()
