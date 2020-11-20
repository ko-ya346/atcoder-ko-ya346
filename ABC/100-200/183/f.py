import numpy as np
import numba
from numba import njit, b1, i4, i8, f8


@njit
def main():
    dp = np.zeros((H, W))
    # 空中にいる場合
    dp1 = np.zeros((H, W, 3))
    dp[0, 0] = 1

    for h in range(H):
        for w in range(W):
            # 壁
            if wall[h, w]:
                continue
            if h:
                x = dp[h-1, w] + dp1[h-1, w, 0]
                dp[h, w] += x
                dp1[h, w, 0] += x
            if w:
                x = dp[h, w-1] + dp1[h, w-1, 1]
                dp[h, w] += x
                dp1[h, w, 1] += x
            if h and w:
                x = dp[h-1, w-1] + dp1[h-1, w-1, 2]
                dp[h, w] += x
                dp1[h, w, 2] += x
            dp[h, w] %= mod
            dp1[h, w] %= mod
    return int(dp[-1, -1])


H, W = map(int, input().split())
wall = np.zeros((H, W), np.bool_)
for h in range(H):
    wall[h] = np.array(list(input()))=="#"

mod = 10**9+7

print(main())