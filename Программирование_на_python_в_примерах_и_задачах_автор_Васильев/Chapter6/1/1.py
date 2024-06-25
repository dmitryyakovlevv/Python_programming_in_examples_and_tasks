l1 = [1, 2, 3, 4]
l2 = [1, 2, 3]


def f(a, b):
    s = 0
    if len(a) > len(b):
        i = 0
        while len(a) != len(b):
            b.append(b[i])
            i += 1
        for i in range(len(a)):
            s += a[i] * b[i]

    else:
        i = 0
        while len(a) != len(b):
            a.append(a[i])
            i += 1
        for i in range(len(b)):
            s += a[i] * b[i]
    print(l1)
    print(l2)
    print(s)


f(l1, l2)