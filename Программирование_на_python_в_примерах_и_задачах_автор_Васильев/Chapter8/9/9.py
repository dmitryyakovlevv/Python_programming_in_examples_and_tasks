def create(N):
    lst = []

    class MyClass:
        def __init__(self, name, n=1):
            self.name = name
            if n == 1:
                self.next = None
            else:
                self.next = MyClass(self.name, n-1)
            self.set(n)

        def set(self, num=1):
            lst.append(self.name + " [" + str(num) + "]")

    test = MyClass("MyClass", N)
    return lst


def append(xlist, n):
    lst = xlist
    for k in range(n):
        lst.append("MyClass "+"["+str(lst.index(lst[len(lst)-1])+2)+"]")
    return lst


a = create(3)
print(a)
b = append(a, 3)
print(b)