N, M = map(int, input().split())

A = [[0, 0] for _ in range(N)]

for _ in range(M):
    p, s = input().split()
    if s == "AC":
        if not A[int(p)-1][0]:
            A[int(p)-1][0] = 1
    else:
        if not A[int(p)-1][0]:
            A[int(p)-1][1] += 1

ans = [0, 0]
for ac, wa in A:
    if ac:
        ans[0] += 1
        ans[1] += wa

print(*ans)