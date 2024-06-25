class Test:
    def __init__(self, lst):
        self.lst = lst


t1 = Test([1, 2, 3])
t2 = Test([1, 2, 3, 4, 5])


def generator(x1, x2):
    if len(x1.lst) > len(x2.lst):
        for d in range(len(x1.lst) - len(x2.lst)):
            x2.lst.append(0)
    elif len(x1.lst) < len(x2.lst):
        for d in range(len(x2.lst) - len(x1.lst)):
            x1.lst.append(0)
    new_lst = []
    for i in range(len(x1.lst)):
        new_lst.append(x1.lst[i] + x2.lst[i])

    return Test(new_lst)


print(generator(t1, t2).__dict__)
