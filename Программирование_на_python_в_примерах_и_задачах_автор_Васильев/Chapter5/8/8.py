text1 = "zbpacdmeoiuay"
slist = ["a", "e", "i", "o", "u", "y"]
glist = ["b", "c", "d", "f", "g", "k", "l", "m", "n", "p", "r", "s", "t", "j", "h", "q", "v", "w", "x", "z"]


def shfr(text_):
    new_text = ""
    for i in range(len(text1)):
        if text_[i] in slist:
            if text_[i] == slist[len(slist) - 1]:
                new_text += slist[0]
            else:
                for j in range(len(slist)-1):
                    if text_[i] == slist[j]:
                        new_text += slist[j+1]
                        break
        elif text_[i] in glist:
            if text_[i] == glist[len(glist) - 1]:
                new_text += glist[0]
            else:
                for j in range(len(glist)-1):
                    if text_[i] == glist[j]:
                        new_text += glist[j+1]
                        break
    return new_text


def dshfr(text_):
    new_text = ""
    for i in range(len(text1)):
        if text_[i] in slist:
            if text_[i] == slist[0]:
                new_text += slist[len(slist) - 1]
            else:
                for j in range(1, len(slist)):
                    if text_[i] == slist[j]:
                        new_text += slist[j-1]
                        break
        elif text_[i] in glist:
            if text_[i] == glist[0]:
                new_text += glist[len(glist) - 1]
            else:
                for j in range(1, len(glist)):
                    if text_[i] == glist[j]:
                        new_text += glist[j-1]
                        break
    return new_text


print(text1)
print(shfr(text1))
print(dshfr(shfr(text1)))