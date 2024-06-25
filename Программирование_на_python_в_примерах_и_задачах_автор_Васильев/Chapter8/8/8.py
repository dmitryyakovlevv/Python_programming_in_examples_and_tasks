def create(N):
    class MyClass:
        def __init__(self, name, n=1):
            self.code = None
            self.name = name
            if n == 1:
                self.next = None
            else:
                self.next = MyClass(self.name, n-1)

            self.set()

        def set(self, num=1):
            self.code = self.name + " [" + str(num) + "]"
            if self.next is not None:
                self.next.set(num + 1)

        def show(self):
            print(self.code)
            if self.next is not None:
                self.next.show()

    return MyClass("MyClass", N)


a = create(7)
a.show()