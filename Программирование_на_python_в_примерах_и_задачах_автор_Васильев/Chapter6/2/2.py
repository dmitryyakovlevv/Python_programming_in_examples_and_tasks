l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(a):
    l_ = []
    for i in range(len(a)):
        if a[i] % 2 != 0:
            l_.append(a[i])
    return l_


print(f(l1))