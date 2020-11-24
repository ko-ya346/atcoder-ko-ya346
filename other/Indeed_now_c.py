n = int(input())
S = sorted([int(input()) for _ in range(n)], reverse=True)
q = int(input())
for _ in range(q):
    k = int(input())
    if k >= n:
        ans = 0
    elif S[k] == 0:
        ans = S[k]
    else:
        ans = S[k] + 1
    print(ans)

