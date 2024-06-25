text = "ABCABD"
l = []
for i in set(text):
    for j in text:
        if i == j:
            k = list(text)
            k.remove(j)
            l.append(tuple(k))
            break
s = dict(zip(set(text), l))
print(s)