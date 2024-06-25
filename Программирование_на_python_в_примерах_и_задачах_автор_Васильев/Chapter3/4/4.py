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


a = mass(4, 4)
print(a)
show(a)