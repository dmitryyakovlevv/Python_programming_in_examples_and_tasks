class A:
    def __init__(self):
        self.a = 0

    def get(self):
        print("Поле класса А:", self.a)


class B(A):
    def __init__(self, x1, x2):
        self.a = x1
        self.b = x2

    def get(self):
        print("Поля класса В:", self.a, self.b)


class C(B):
    def __init__(self, x1, x2, x3):
        self.a = x1
        self.b = x2
        self.c = x3

    def get(self):
        print("Поля класса C:", self.a, self.b, self.c)


a = A()
a.get()

b = B(1, 2)
b.get()


c = C(3, 1, 2)
c.get()