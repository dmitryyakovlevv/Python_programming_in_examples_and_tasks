a = int(input("Введите число "))
b = int(input("Введите число "))
m = set()
print(a, ": ", sep="", end="")
while a != 0:
    m.add(a % 10)
    a //= 10
print(m)
l = list()
print(b, ": ", sep="", end="")
while b != 0:
    l.append(b % 10)
    b //= 10
l = list(reversed(l))


def ch(A):
    for i in range(len(A)):
        for j in range(1, len(A)-i):
            if A[i] == A[i+j]:
                A[i + j] = []
    return A


print(ch(l))