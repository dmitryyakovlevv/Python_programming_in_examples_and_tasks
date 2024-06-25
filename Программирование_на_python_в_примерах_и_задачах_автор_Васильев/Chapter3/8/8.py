from random import *


def sortV(L):
    b = False
    while b != True:
        b = True
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                k = L[i]
                L[i] = L[i+1]
                L[i+1] = k
                b = False
    return L


def sortU(L):
    b = False
    while b != True:
        b = True
        for i in range(len(L)-1):
            if L[i] < L[i+1]:
                k = L[i]
                L[i] = L[i+1]
                L[i+1] = k
                b = False
    return L


def order(L):
    lch = []
    lnch = []
    for i in range(len(L)):
        if L[i] % 2 == 0:
            lch.append(L[i])
            L[i] = 0
        else:
            lnch.append(L[i])
            L[i] = 1
    lch = sortV(lch)
    lnch = sortU(lnch)
    i = 0
    j = 0
    for k in range(len(L)):
        if L[k] == 0:
            L[k] = lch[i]
            k += 1
            i += 1
        else:
            L[k] = lnch[j]
            k += 1
            j += 1
    return L


l = [randint(1, 9) for i in range(0, 10)]
print(l)
print(order(l))