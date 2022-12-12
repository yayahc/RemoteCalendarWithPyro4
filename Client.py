# Client
# @author : yayahc
# @version : 1.0

import Pyro4
import time

uri = input("What is the Pyro URI? ").strip()

maker = Pyro4.Proxy(uri)

def calendar():
    return "Calendar ->\Year: {}\nMonth: {}\nDay: {}".format(maker.getAnnee(),maker.getMois(),maker.getJour())

def menu():
    return "-----Menu-----\n1 - Get\n2 - Exit\n"


file = open('./pil/MyArt.txt', 'r')
content = file.read()
#print(content)
file.close()
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
