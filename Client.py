# Client
# @author : yayahc
# @version : 1.2

import Pyro4
import time

uri = input("What is the Pyro Uri? ").strip()

pyroProxy = Pyro4.Proxy(uri)

def calendar():
    return "Calendar ->\nYear: {}\nMonth: {}\nDay: {}".format(pyroProxy.getYear(),pyroProxy.getMonth(),pyroProxy.getDay())

def menu():
    return "-----Menu-----\n1 - Get\n2 - Exit\n"


print("Login...")
time.sleep(2)
print("Welcome to RemoteCalendar...")
print(menu())

while True:
    user_answer = input('? ')
    if user_answer == "1":
        print(calendar())
        break
    elif user_answer == "2":
        print('Logout...')
        time.sleep(2)
        break
    else:
        print(menu())