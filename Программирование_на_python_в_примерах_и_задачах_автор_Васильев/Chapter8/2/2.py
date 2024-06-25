class first:
    def __init__(self, x1, x2):
        if type(x1) == str and type(x2) == str:
            self.txt = x1 + x2
            print("Поле создано:", self.txt)
        elif type(x1) == int and type(x2) == int:
            self.number = x1 + x2
            print("Поле создано:", self.number)
        else:
            print("Поле не создано")


a = first("hello ", "world")
b = first(0, 1)
c = first("hello", 0)