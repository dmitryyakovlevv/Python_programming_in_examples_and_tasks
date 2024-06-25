text1 = "rtr rtr dhd http cd "
lstT = []
txt = ""
for i in range(len(text1)-1):
    if text1[i] == " ":
        txt = ""
    else:
        txt += text1[i]
        if text1[i+1] == " " or text1[i+1] == "":
            lstT.append(txt)
lstT.reverse()
print(lstT)
