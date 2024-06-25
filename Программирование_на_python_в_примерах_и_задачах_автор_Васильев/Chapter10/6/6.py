from threading import *
from time import sleep


def mysum():
    global num
    k = 1
    txt = str(num)
    while myevent.is_set():
        num += k**2
        txt += "+"+str(k**2)
        print("[", k, "]", txt, "=", num, sep="")
        k += 1
        sleep(0.5)


print("Сумма:")

t = Thread(target=mysum)
num = 0

myevent = Event()
myevent.set()

t.start()
sleep(1)

myevent.clear()

if t.is_alive():
    t.join()
print("Результат:", num)