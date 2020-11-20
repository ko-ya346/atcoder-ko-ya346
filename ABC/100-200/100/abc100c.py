from functools import reduce
from operator import mul

n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in a:
    count = 0
    while i%2 == 0:
        count += 1
        i = i/2
    ans += count

print(ans)