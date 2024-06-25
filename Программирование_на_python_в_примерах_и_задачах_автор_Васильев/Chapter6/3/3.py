def f(*n):
    return min(n), max(n), sum(n)/len(n)


print(f(1, 2, 3, 4, 5, 6))