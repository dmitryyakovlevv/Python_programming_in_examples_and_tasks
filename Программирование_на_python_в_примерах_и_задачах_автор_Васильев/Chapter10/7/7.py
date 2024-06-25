from threading import *
from time import sleep


def First():
    global i, L
    val = "A"
    while True:
        if i % 2 == 0:
            L[i] = val
            val = chr(ord(val)+1)
            i += 1
            sleep(0.3)
        else:
            break


def Second():
    global i, L
    val = 0
    while True:
        if i % 2 != 0:
            L[i] = val
            val += 1
            i += 1
            sleep(0.3)
        else:
            break


L = ["*" for k in range(11)]
i = 0
print("Список до заполнения:")
print(L)

A = Thread(target=First)
B = Thread(target=Second)

A.start()
B.start()

A.join()
B.join()

print("Список после заполнения:")
print(L)