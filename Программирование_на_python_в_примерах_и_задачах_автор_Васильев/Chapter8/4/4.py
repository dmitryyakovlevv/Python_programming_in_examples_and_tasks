def create(fields, vals, name=None):
    if type(name) != str:
        name = "X"
    if type(fields) != list or type(vals) != list:
        class MyClass:
            def show(self):
                print("Объект без полей")
                print("Класс", self.__class__.__name__)
    else:
        class MyClass:
            def __init__(self):
                k = 0
                for f in fields:
                    self.__dict__[f] = vals[k]
                    k += 1

            def show(self):
                print("Объект с полями")
                for f in dir(self):
                    if not f.startswith("_") and f != "show":
                        print(f, self.__dict__[f])
                print("Класс", self.__class__.__name__)
    MyClass.__name__ = name
    return MyClass()


A = create(["red", "green", "blue"], [1, 2, 3], "MyColors")
A.show()
B = create(["red", "green", "blue"], [1, 2, 3])
B.show()
C = create(1, 2, 3)
C.show()