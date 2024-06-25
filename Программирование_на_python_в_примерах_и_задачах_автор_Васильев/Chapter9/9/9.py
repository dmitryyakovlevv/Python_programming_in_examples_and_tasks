class New:
    def __init__(self, n):
        self.lst = [i for i in range(1, n*2 + 1) if i % 2 != 0]
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < len(self.lst):
            return self.lst[self.position]
        else:
            raise StopIteration


A = New(4)
try:
    while True:
        print(next(A), end=" ")
except StopIteration:
    print()