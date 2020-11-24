from collections import deque

n, m = map(int, input().split())
friend = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    friend[a].append(b)
    friend[b].append(a)


def bfs(que):
    while que:
        x = que.popleft()
        for nx in friend[x]:
            if seen[nx] >= 0:
                continue
            que.append(nx)
            seen[nx] = seen[x] + 1
for i in range(n):
    seen = [-1 for _ in range(n)]

    if seen[i] >= 0:
        continue
    que = deque([i])
    seen[i] = 0
    bfs(que)
    print(seen.count(2))