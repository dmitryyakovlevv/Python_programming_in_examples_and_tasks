print("Введите целое число")
x = int(input())
a = []
while x != 0:
    k = x % 10
    a.append(k)
    x = x // 10
a_ = tuple(a)
a__ = tuple(reversed(a_))
print(a__)
print(a_)