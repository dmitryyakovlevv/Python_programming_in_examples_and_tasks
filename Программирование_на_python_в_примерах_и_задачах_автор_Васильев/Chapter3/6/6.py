from random import *
print("Введите количество злементов в массиве")
n = int(input())
l = [randint(0, 9) for i in range(0, n)]
b = False
print(l)
while b != True:  # пока есть перестановка
    b = True  # нет перестановки
    for i in range(0, n-1):  # n-1 тк существует индекс i+1, который как бы заглядывает наперед на один шаг
        if l[i] > l[i + 1]:
            k = l[i + 1]
            l[i + 1] = l[i]
            l[i] = k
            b = False  # произошла перестановка
print(l)