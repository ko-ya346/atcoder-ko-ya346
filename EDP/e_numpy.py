import sys
input = lambda: sys.stdin.buffer.readline().rstrip()
n, w_max = map(int, input().split())
import numpy as np

v,w = [],[]
for i in range(n):
    w_, v_ = map(int, input().split())
    v.append(v_)
    w.append(w_)
dp = np.array([10**10]*(100))
dp[0] = 0
for i in range(n):
    print(dp)
    # print(dp[v[i]:])
    dp[v[i]:] = np.minimum(dp[v[i]:], w[i]+dp[:-v[i]])
ans = 0
for i,w in enumerate(dp):
    print(i)
    if w<= w_max:
        ans = i
print(ans)
