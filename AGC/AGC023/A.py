from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
A = list(map(int, input().split()))

a = [0 for _ in range(N)]
a[0] = A[0]

for i in range(N-1):
    a[i+1] += a[i] + A[i+1]

ans = 0
# print(Counter(a))
for key, val in Counter(a).items():
    if key == 0:
        ans += val
    if val >= 2:
        ans += combinations_count(val, 2)

print(ans)