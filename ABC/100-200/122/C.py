import sys
import math

N, Q = map(int, input().split())
S = input()
a = [0 for _ in range(N)]

for i in range(1, N):
    if S[i-1]+S[i] == "AC":
        a[i] += 1 + a[i-1]
    else:
        a[i] += a[i-1]

for _ in range(Q):
    l, r = map(int, sys.stdin.readline().strip().split())
    print(a[r-1] - a[l-1])
