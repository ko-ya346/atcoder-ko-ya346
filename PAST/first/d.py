from collections import Counter

N = int(input())
a = [int(input()) for _ in range(N)]
per = list(range(1, N+1))

l = Counter(a)
ans = 0

for i, v in l.items():
    if v == 2:
        ans = i
# print(ans)

if not ans:
    print("Correct")
else:
    sa = list(set(per) - set(a))[0]

    print(ans, sa)