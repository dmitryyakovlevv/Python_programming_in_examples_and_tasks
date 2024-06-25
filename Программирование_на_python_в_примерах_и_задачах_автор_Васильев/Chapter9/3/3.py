class New:
    def __init__(self, mass):
        self.lst = mass

    def __add__(self, other):
        if type(other) == type(self):
            self.lst += other.lst
        return New(self.lst)

    def __str__(self):
        return str(self.lst)


A = New([1, 2])
B = New([3, 4])
print(A+B)