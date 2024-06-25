text1 = "EeAaZzBbCcDd"


def shfr(text_):
    new_text = ""
    for i in range(len(text_)):
        if ord(text_[i]) == ord("B") or ord(text_[i]) == ord("b"):
            new_text += chr(ord(text_[i]) + 24)
        elif ord(text_[i]) == ord("A") or ord(text_[i]) == ord("a"):
            new_text += chr(ord(text_[i]) + 24)
        else:
            new_text += chr(ord(text_[i]) - 2)
    return new_text


def dshfr(text_):
    new_text = ""
    for i in range(len(text_)):
        if ord(text_[i]) == ord("Z") or ord(text_[i]) == ord("z"):
            new_text += chr(ord(text_[i]) - 24)
        elif ord(text_[i]) == ord("Y") or ord(text_[i]) == ord("y"):
            new_text += chr(ord(text_[i]) - 24)
        else:
            new_text += chr(ord(text_[i]) + 2)
    return new_text


print(text1)
print(shfr(text1))
print(dshfr(shfr(text1)))