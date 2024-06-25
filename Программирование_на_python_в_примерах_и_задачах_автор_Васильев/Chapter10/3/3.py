def F(A, B):
    try:
        if A-1 == 0 and B == 0:
            print("Решение любое число")
        else:
            x = B/((A**2) - 1)
            print(x)
    except ArithmeticError:
        print("Решений нет")
    except:
        print("Что-то пошло не так")


F(2, 3)