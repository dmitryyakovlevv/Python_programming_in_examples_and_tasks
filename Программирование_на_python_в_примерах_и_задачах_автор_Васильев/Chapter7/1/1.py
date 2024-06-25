x = int(input("введите число в десятичной системе счисления "))
n = int(input("введите основание для системы счисления "))
if n < 10:
    s_ = []
    while x > n-1:
        s_.append(x % n)
        x = x // n
    s_.append(x)
    s_.reverse()
    print(s_)
elif n == 10:
    print(x)
else:
    print("только для систем счисления меньше 11")