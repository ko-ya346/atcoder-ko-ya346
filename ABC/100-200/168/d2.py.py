from collections import deque

N, M = map(int, input().split())

route = [[] for _ in range(N)]
used = [-1] * N
used[0] = 0

for _ in range(M):
    a, b = map(int, input().split())
    route[a-1].append(b-1)
    route[b-1].append(a-1)

queue = deque([0])

def bfs(queue):
    while queue:
        v = queue.popleft()
        for nv in route[v]:
            if used[nv] != -1:
                continue
            used[nv] = v+1
            queue.append(nv)

bfs(queue)

for i, v in enumerate(used):
    if i == 0:
        print("Yes")
    else:
        print(v)
# print(used)