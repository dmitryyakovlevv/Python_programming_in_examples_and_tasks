try:
    a = int(input("Введите число "))
    b = int(input("Введите число "))
    for i in range(a, b+1):
        print(i, end=" ")
except:
    print("Error")