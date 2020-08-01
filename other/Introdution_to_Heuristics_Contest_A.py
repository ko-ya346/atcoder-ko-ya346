from bisect import bisect_left
from random import randint

D = int(input())
C = list(map(int, input().split()))

S = [list(map(int, input().split())) for _ in range(D)]

last = [0]*26
ans = 0

for d in range(D):
    mx = -3650000
    mxt = -1
    #適当な数字を選ぶ
    for j in range(26):
        tmp = last[j]
        last[j] = d+1
        score = S[d][j]
        #スコア計算
        for i in range(26):
            score -= C[i]*(d-last[i])

        if mx < score:
            mxt = j
            mx = score
        last[j] = tmp
    last[mxt] = d+1
    
    print(mxt + 1)