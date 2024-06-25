class New:
    def __init__(self, num):
        self.val = num

    def __str__(self):
        return str(self.val)

    def __add__(self, other):
        self.val += other
        return New(self.val)

    def __sub__(self, other):
        self.val -= other
        return New(self.val)

    def __rsub__(self, other):
        other -= self.val
        return New(other)

    def __mul__(self, other):
        self.val *= other
        return New(self.val)

    def __truediv__(self, other):
        self.val /= other
        return New(self.val)


A = New(5)
print(A+1)
print(A-1)
print(1-A)
print(A*5)
print(A/5)
