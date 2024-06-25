class OldClass:
    def __init__(self):
        self.x1 = 1
        self.x2 = 2


def create(TestClass):
    obj = TestClass()

    class NewClass:
        def __init__(self):
            for f in dir(obj):
                if not f.startswith("_"):
                    self.__dict__[f] = obj.__dict__[f]
            self.x3 = 3
    return NewClass


print("Существующий объект класса", OldClass().__dict__)
print("Новый объект класса на основе существующего класса", create(OldClass)().__dict__)


# РЕШЕНИЕ С ИСПОЛЬЗОВАНИЕМ ДЕКОРАТОРА,ВЫВОДИТ ТОЖЕ САМОЕ, ПРОВЕРЕННО

# def create(TestClass):
#     obj = TestClass()
#
#     class NewClass:
#         def __init__(self):
#             for f in dir(obj):
#                 if not f.startswith("_"):
#                     self.__dict__[f] = obj.__dict__[f]
#             self.x3 = 3
#     return NewClass
#
#
# @create
# class OldClass:
#     def __init__(self):
#         self.x1 = 1
#         self.x2 = 2
#
#
# print("Существующий объект класса", OldClass().__dict__)
# print("Новый объект класса на основе существующего класса", OldClass().__dict__)