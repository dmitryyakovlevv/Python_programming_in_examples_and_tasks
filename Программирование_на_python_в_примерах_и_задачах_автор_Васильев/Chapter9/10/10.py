class New:
    def __init__(self, n):
        L = [1, 1]
        a = 1
        b = 1
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
            # a, b = b, a+b
            L.append(b)
        self.lst = L
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < len(self.lst):
            return self.lst[self.position]
        else:
            raise StopIteration


A = New(7)
try:
    while True:
        print(next(A), end=" ")
except StopIteration:
    print()