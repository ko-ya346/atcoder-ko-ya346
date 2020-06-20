import numpy as np

N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

ans = 0

for i in range(60):
    cnt = 0
    for a in A:
        cnt += a>>i&1
    ans += cnt*(N-cnt)*2**i
    ans %= mod
    # print(ans)
print(ans)
