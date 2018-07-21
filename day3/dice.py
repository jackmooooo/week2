import random
from time import sleep
def d2():
    x = random.randint(1, 20)
    for i in range(x):
        time.sleep(200)
        if i = x-1:
            print("")
        print(random.randint(1, 2))
def d3():
    x = random.randint(1, 20)
    for i in range(x):
        time.sleep(20)
        if i = x-1:
            print("")
        print(random.randint(1, 3))
def d4():
    x = random.randint(1, 50)
    for i in range(x):
        time.sleep(2)
        if i = x-1:
            print("")
        print(random.randint(1, 4))
def d6():
    random.randint(1, 50)
    for i in range(x):
        time.sleep(2)
        if i = x-1:
            print("")
        print(random.randint(1, 6))
def d8():
    x = random.randint(1, 50)
    for i in range(x):
        time.sleep(2)
        if i = x-1:
            print("")
        print(random.randint(1, 8))
def d10():
    x = random.randint(1, 100)
    for i in range(x):
        time.sleep(1)
        if i = x-1:
            print("")
        print(random.randint(1, 10))
def d12():
    x = random.randint(1, 100)
    for i in range(x):
        time.sleep(1)
        if i = x-1:
            print("")
        print(random.randint(1, 12))
def d20():
    x = random.randint(1, 100)
    for i in range(x):
        time.sleep(1)
        if i = x-1:
            print("")
        print(random.randint(1, 20))
def d100():
    x = random.randint(1, 100)
    for i in range(x):
        time.sleep(1)
        if i = x-1:
            print("")
        print(random.randint(1, 100))
def d120():
    x = random.randint(1, 120)
    for i in range(x):
        time.sleep(1)
        if i = x-1:
            print("")
        print(random.randint(1, 120))

def directory():
    true = True
    while true:
        print("")
        inp1 = input("what dice woule you like to roll  >> ")
        print("")
        if inp1 == "d2":
            d2()
        elif inp1 == "d3":
            d3()
        elif inp1 == "d4":
            d4()
        elif inp1 == "d6":
            d6()
        elif inp1 == "d8":
            d8()
        elif inp1 == "d10":
            d10()
        elif inp1 == "d12":
            d12()
        elif inp1 == "d20":
            d20()
        elif inp1 == "d100":
            d100()
        elif inp1 == "d120":
            d120()
        elif inp1 == "cancel":
            true = False
        elif inp1 == "end":
            true = False

directory()
