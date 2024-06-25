def F(*n):
    try:
        k = 0
        for s in n:
            if type(s) == int:
                k += s
        return k

    except:
        return "Error"


print(F(1, 2, 3, "dkd", [1, 3, 2], 4))