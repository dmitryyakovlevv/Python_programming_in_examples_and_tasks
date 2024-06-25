from random import *
n = 3
l = [randint(0, 9) for i in range(0, n)]
print(l)
res = []
for i in range(len(l)-1):
    res.append(l[i]+l[i+1])
k = 0
for i in range(len(l)+1):
    if l.index(l[i]) % 2 != 0:
        l.insert(i, res[k])
        k += 1
print(res)
print(l)