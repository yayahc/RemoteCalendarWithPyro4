# Client
# @author : yayahc
# @version : 1.0

import Pyro4
import time

uri = input("What is the Pyro URI? ").strip()

maker = Pyro4.Proxy(uri)

def calendar():
    return "Calendar ->\nAnnee: {}\nMois: {}\nJour: {}".format(maker.getAnnee(),maker.getMois(),maker.getJour())

def menu():
    return "-----Menu-----\n1 - Get Calendar\n2 - Exit\n"

print("Welcome to CalendrierDistant...")
print("login ...")
time.sleep(2)
print(menu())

while True:
    user_answer = int(input('? '))
    if user_answer == 1:
        print(calendar())
        break
    elif user_answer == 2:
        print('logout...')
        time.sleep(2)
        break
    else:
        print(menu())