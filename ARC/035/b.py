from itertools import accumulate
from collections import Counter

n = int(input())
T = [int(input()) for _ in range(n)]
t = list(accumulate(accumulate(sorted(T))))[-1]
mod = 10**9+7
print(t)

def factorial_cor(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
        fact %= mod
    return fact

ans = 1
for k, v in dict(Counter(T)).items():
    ans = ans * factorial_cor(v) % mod

print(ans)