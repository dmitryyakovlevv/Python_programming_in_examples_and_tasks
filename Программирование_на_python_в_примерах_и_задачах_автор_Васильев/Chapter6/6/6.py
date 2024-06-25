def F(f, n, a):
    # n количество повторов, a число, f функция
    if n == 0:
        return a
    else:
        s = f(a)
        return F(f, n - 1, s)


print(F(lambda x: x * 2, 3, 1))
