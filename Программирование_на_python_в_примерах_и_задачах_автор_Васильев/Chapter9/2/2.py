class A:
    def __init__(self, val):
        self.x = val

    def __str__(self):
        return str(self.x)

    def __int__(self):
        return int(self.x)

    def __float__(self):
        return float(self.x)


a = A(100)
print(int(a)-1)
print(float(a)+1.0)
print(str(a) + "!")

