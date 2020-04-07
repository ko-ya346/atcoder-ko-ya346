import math
from functools import reduce

def gcd(numbers):
    return reduce(math.gcd, numbers)

n = int(input())
a = list(map(int, input().split()))

ans = []
if len(a) != 1:
    ans.append(gcd(a[1:]))
    ans.append(gcd(a[:n]))

    for i in range(1, n-1):
        aaaa = []
        aaaa.append(gcd(a[:i]))
        aaaa.append(gcd(a[i+1:]))
        ans.append(gcd(aaaa))
else:
    ans.append(a[0])
    
print(max(ans))
