from collections import Counter

N = int(input())
S = list(input())

ans = 1
for v in Counter(S).values():
    ans *= v+1
print(ans-1)