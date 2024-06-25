def f(*n, txt=""):
    text_ = ""
    for i in n:
        text_ += txt[i]
    return text_


print(f(0, 2, 5, txt="abcdefg"))