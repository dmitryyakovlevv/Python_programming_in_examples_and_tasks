from fractions import Fraction
a = Fraction(1, 3)
b = Fraction(2, 3)
l = [a+b, a-b, a*b, a/b]
print("a+b =", a+b)
print("a-b =", a-b)
print("a*b =", a*b)
print("a/b =", a/b)
print("min =", min(l))
print("max =", max(l))
