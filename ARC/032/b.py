from collections import deque

n, m = map(int, input().split())
traffic = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    traffic[a].append(b)
    traffic[b].append(a)

seen = [False for _ in range(n)]

def bfs(que):
    while que:
        x = que.popleft()
        seen[x] = True
        for nx in traffic[x]:
            if seen[nx]:
                continue
            que.append(nx)

ans = -1
for i in range(n):
    if seen[i]:
        continue
    que = deque([i])
    bfs(que)
    ans += 1
print(ans)

