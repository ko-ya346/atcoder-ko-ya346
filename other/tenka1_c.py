N = int(input())
S = list(input())
S1 = S.copy()
S.reverse()
S2 = S.copy()

f = 0
ans1 = 0

for i in range(N):
    if S1[i] == "#":
        f = 1
    else:
        if f:
            ans1 += 1
            S1[i] = "#"

ans2 = 0
f = 0

for i in range(N):
    print(S2[i])
    if S2[i] == ".":
        f = 1
    else:
        if f:
            ans2 += 1
            S2[i] = "."
print(ans1, ans2)
