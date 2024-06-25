text_ = "123456789"
text1 = list(text_)
text = ""
for i in range(0, len(text1)-1):
    if i == 0 or i % 3 == 0:
        k = text1[i]
        text1[i] = text1[i+2]
        text1[i+2] = k
for i in range(len(text1)):
    text += str(text1[i])

print(text)