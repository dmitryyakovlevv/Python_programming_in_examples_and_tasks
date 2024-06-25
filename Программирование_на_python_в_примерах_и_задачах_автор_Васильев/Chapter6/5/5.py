def F(f, a, b):
    lst = []
    for i in range(a, b+1):
        lst.append(f(i))
    return max(lst)


def h(x):
    return x+1


print(F(h, 0, 1))