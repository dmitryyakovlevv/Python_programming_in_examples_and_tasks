n = int(input("Введите целое неотрицательное число: "))
l = [i for i in range(1, n+1)]
l.reverse()
s = dict((i, l.index(i)+1) for i in l)
print(s)