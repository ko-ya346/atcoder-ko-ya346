from collections import Counter

N = int(input())
S = sorted(Counter([input() for _ in range(N)]).items(), key=lambda x: x[0])
S = sorted(S, key=lambda x: x[1], reverse=1)
cnt_max = S[0][1]
# print(cnt_max)
for i, v in S:
    if v == cnt_max:
        print(i)
