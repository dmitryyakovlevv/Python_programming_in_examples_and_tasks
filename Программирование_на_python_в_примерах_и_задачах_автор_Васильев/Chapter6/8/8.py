def f(a, s=1, n=1):
    if s > 20:
        print("")
    else:
        print(n, s)
        n *= a
        s += n
        return f(a, s, n)


f(3)
