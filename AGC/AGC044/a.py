# T = int(input())

# for _ in range(T):
N, A, B, C, D = map(int, input().split())

cost = 0

if B*3 > C*5:
    div = 5
    cos = C
else:
    div = 3
    cos = B

mod = N%div
if mod > div-mod:
    N += div-mod
else:
    n -= mod

cost += N//div *B
N 