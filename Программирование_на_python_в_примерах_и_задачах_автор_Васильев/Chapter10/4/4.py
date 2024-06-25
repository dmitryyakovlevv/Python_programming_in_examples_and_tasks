import math


def F(A):
    try:
        if A == 0:
            print(-1)
        else:
            x = math.sin(A)/(A*(A - 1))
            print(x)
    except ArithmeticError:
        print("Решений нет")


F(2)