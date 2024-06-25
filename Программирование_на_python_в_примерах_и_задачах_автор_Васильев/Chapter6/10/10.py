def f(x):
    for n in range(x+1):
        yield 2**n


for i in f(5):
    print(i)