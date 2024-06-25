from threading import *

lst = [[0, 1, 2, 3], [4, 5, 6, 7], [4, 5, 6, 7]]


def setl():
    global i
    for j in range(len(lst[i])):
        lst[i][j] = "*"
    i += 1


i = 0
t1 = Thread(target=setl)
t2 = Thread(target=setl)
t3 = Thread(target=setl)
print("Потоки начинают выполнение")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Потоки закончили выполнение")
print(lst)