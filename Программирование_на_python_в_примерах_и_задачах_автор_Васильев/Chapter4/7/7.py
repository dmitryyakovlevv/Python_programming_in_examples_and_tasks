text = "ABBCAB"
s = dict.fromkeys(set(text), 0)
for k in s.keys():
    for i in range(len(text)):
        if k == text[i]:
            s[k] += 1
print(s)

