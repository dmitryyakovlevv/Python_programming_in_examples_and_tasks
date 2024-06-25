text1 = "EeAaZzBbCcDd"


def shfr(text_):
    new_text = ""
    for i in range(len(text_)):
        if ord(text_[i]) == ord("A") or ord(text_[i]) == ord("a"):
            new_text += chr(ord(text_[i]) + 25)
        elif ord(text_[i]) == ord("Z") or ord(text_[i]) == ord("z"):
            new_text += chr(ord(text_[i]) - 25)
        else:
            new_text += chr(ord(text_[i]) + 1)
    return new_text


def dshfr(text_):
    new_text = ""
    for i in range(len(text_)):
        if ord(text_[i]) == ord("A") or ord(text_[i]) == ord("a"):
            new_text += chr(ord(text_[i]) + 25)
        elif ord(text_[i]) == ord("Z") or ord(text_[i]) == ord("z"):
            new_text += chr(ord(text_[i]) - 25)
        else:
            new_text += chr(ord(text_[i]) - 1)
    return new_text


print(text1)
print(shfr(text1))
print(dshfr(shfr(text1)))
