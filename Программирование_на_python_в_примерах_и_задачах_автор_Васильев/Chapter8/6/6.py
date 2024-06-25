from random import randint


class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def create(n):
    lst = []
    for i in range(n):
        x = randint(0, 10)
        if x % 2 != 0:
            lst.append(Test(x, x+2).__dict__)
        else:
            lst.append(Test(x + 1, x + 3).__dict__)
    return lst


print(create(3))
