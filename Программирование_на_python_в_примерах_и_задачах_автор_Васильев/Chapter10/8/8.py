from threading import *


class Myclass:
    def __init__(self, x1, x2):
        self.lst1 = ["*" for k in range(x1)]
        self.lst2 = ["*" for k in range(x2)]


obj = Myclass(5, 5)


def first():
    s = ord("A")
    for i in range(len(obj.lst1)):
        obj.lst1[i] = chr(s)
        s += 1
    print(obj.lst1)


def second():
    s = 0
    for i in range(len(obj.lst2)):
        obj.lst2[i] = s
        s += 1
    print(obj.lst2)


t1 = Thread(target=first)
t2 = Thread(target=second)

print("Потоки начинают выполнение")
t1.start()
t2.start()

t1.join()
t2.join()
print("Потоки закончили выполнение")
