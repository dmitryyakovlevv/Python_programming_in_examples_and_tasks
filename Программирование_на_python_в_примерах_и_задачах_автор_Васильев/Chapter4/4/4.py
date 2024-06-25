m1 = {i for i in range(1, 51) if i % 3 == 0 or i % 4 == 0}
m2 = {i for i in range(1, 51) if i % 3 == 0 and i % 4 == 0}
print(m1 - m2)