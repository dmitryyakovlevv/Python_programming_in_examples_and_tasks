class New:

    def __setattr__(self, name, val):
        res = ""
        if type(val) == list:
            for s in val:
                if type(s) == str:
                    res += s.replace(s, s[0])
                else:
                    del s
        self.__dict__[name] = res


A = New()
A.lst = [1, 2, "I", 3, "Say", "Hello", 1223.0, "World"]
print(A.lst)
