from random import *
l = [randint(0, 9) for i in range(0, 10)]
l_ = [max(l), l.index(max(l))]
print(l)
print(l_)