from threading import *


def factorial():
    global n
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)


def double_factorial():
    global n
    f = 1
    for i in range(1, n+1, 2):
        f *= i
    print(f)


def fib():
    global n
    a = 1
    b = 1
    for i in range(n-2):
        c = a+b
        a = b
        b = c
    print(b)


n = 5
t1 = Thread(target=factorial)
t2 = Thread(target=double_factorial)
t3 = Thread(target=fib)
print("Потоки начинают выполнение")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Потоки закончили выполнение")