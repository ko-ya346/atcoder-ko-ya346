from math import gcd

a = 24
b = 18

print(gcd(a, b))


def gcd1(x, y):
    if y == 0:
        return x
    return gcd1(y, x%y)

print(gcd1(a, b))