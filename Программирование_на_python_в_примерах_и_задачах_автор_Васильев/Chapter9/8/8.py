class New:
    def __init__(self):
        self.lst = [1, 2, 3, 4]

    def __call__(self, n):
        s = 0
        for i in range(len(self.lst)):
            s += self.lst[i]*n**i
        return s


A = New()
print(A(1))