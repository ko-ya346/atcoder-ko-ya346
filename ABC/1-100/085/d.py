N, H = map(int, input().split())

A = []
B = []
a_max = 0
for _ in range(N):
    a, b = map(int, input().split())
    a_max = max(a, a_max)
    A.append(a)
    B.append(b)

B = sorted(B, reverse=True)

ans = 0
f = 0

for i in B:
    if i < a_max:
        continue
    ans += 1
    H -= i
    if H <= 0:
        f = 1
        break

if f:
    print(ans)
else:
    if H%a_max == 0:
        print(ans + H//a_max)
    else:
        print(ans + H//a_max+1)