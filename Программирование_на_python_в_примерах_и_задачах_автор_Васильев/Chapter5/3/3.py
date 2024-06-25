text = "A_smCNagz"
text1 = ""
delta = ord("a") - ord("A")
for i in range(len(text)):
    if ord(text[i]) in range(ord("A"), ord("Z")+1):
        text1 += chr(ord(text[i]) + delta)
    elif ord(text[i]) in range(ord("a"), ord("z")+1):
        text1 += chr(ord(text[i]) - delta)
    else:
        text1 += text[i]
print(text1)