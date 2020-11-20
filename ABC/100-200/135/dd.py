import numpy as np
from numba import njit, i8


@njit(i8(i8[:]), cache=True)
def solve(S):
    MOD = 1_000_000_007
    dp = np.zeros(13, dtype=np.int64)
    tmp = np.zeros(13, dtype=np.int64)
    dp[0] = 1
    for c in S:
        for j in range(10):
            if c != -1 and c != j:
                continue
            for k in range(13):
                tmp[(j + k * 10) % 13] += dp[k]
        dp = tmp % MOD
        tmp.fill(0)
    return dp[5]


S = np.array([-1 if c == "?" else int(c) for c in input()], dtype=np.int64)
print(solve(S))
