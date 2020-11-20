import fractions
from functools import reduce

def gcd(numbers):
    return reduce(fractions.gcd, numbers)

n, x = list(map(int, input().split()))
b = list(map(int, input().split()))

a = []
for i in b:
    if i != x:
        a.append(abs(i-x))
print(gcd(a))