from collections import deque

N, M = map(int, input().split())

E = [[int(x) - 1 for x in input().split()] for _ in range(M)]

ans = 0
for i in range(M):
    G = [[] for _ in range(N)]
    for j in range(M):
        if i==j:
            continue
        a, b = E[j]
        G[a].append(b)
        G[b].append(a)


    que = deque([0])

    check = [-1 for _ in range(N)]

    while que:
        v = que.popleft()
        check[v] = 0
        for i in G[v]:
            if check[i] == -1:
                que.append(i)
    if sum(check) < 0:
        ans += 1
print(ans)
