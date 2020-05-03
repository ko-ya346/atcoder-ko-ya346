from math import gcd
from functools import reduce
from operator import mul

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n, m = list(map(int, input().split()))

a = list(map(int, input().split()))

lcm = lcm_list(a)
print(int((m)//lcm))
