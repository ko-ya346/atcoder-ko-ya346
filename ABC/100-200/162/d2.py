N = int(input())
S = input()

def f(a, b, c):
    if abs(a-b) == abs(a-c) or abs(a-b) == abs(b-c) or abs(b-c) == abs(a-c):
        return 0
    else:
        return 1

cnt = 0
R, B, G = [], [], []
for i in range(N):
    if S[i] == "R":
        R.append(i)
    elif S[i] == "B":
        B.append(i)
    else:
        G.append(i)

for r in R:
    for b in B:
        for g in G:
            if f(r, b, g):
                cnt += 1
# print(R, G, B)
print(cnt)
