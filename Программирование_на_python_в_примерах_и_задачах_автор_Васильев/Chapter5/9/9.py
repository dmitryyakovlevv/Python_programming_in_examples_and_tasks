text1 = "rtr rtr dhd http cd "
lstT = []
lstK = []
k = 0
txt = ""
for i in range(len(text1)-1):
    if text1[i] == " ":
        k = 0
        txt = ""
    else:
        k += 1
        txt += text1[i]
        if text1[i+1] == " " or text1[i+1] == "":
            lstK.append(k)
            lstT.append(txt)
print("Самое длинное слово:", lstT[lstK.index(max(lstK))])





