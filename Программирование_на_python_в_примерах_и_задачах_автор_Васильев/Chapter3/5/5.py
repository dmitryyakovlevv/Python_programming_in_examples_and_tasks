from random import *


def show(A):
    for a in A:
        for s in a:
            print(s, end=" ")
        print()


def mass(n, m):
    res = [["" for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = randint(0, 9)
    return res


def delet(A, n, m):
    for i in range(len(A)):
        for j in range(m-1, m):
            A[i].pop(j)
            #A[i].remove(A[i][j])
    A.pop(n-1)
    return A


l = mass(4, 4)
show(l)
print("Введите номер строки и столбца, которые хотите удалить")
n = int(input())
m = int(input())
a = delet(l, n, m)
show(a)