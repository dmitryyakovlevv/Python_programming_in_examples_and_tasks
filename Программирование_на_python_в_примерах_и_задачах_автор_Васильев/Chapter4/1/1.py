from random import *
m = set()
while len(m) < 5:
    m.add(randint(1, 10))
while len(m) < 15:
    m.add(randint(10, 30))
print(m)