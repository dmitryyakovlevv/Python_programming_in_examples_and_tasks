class MyError(Exception):
    def __init__(self):
        self.values = []

    def __add__(self, val):
        self.values.insert(0, val)
        return self


def getMyError(n):
    try:
        if n <= 1:
            raise MyError
        getMyError(n-1)
    except MyError as error:
        raise error+chr(ord("A")+n-1)


def getList(n):
    try:
        getMyError(n)
    except MyError as error:
        return error.values


A = getList(10)
print(A)