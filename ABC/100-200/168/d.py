from collections import deque

N, M = map(int, input().split())

route = [[] for _ in range(N)]
used = [False] * N
used[0] = True

for _ in range(M):
    a, b = map(int, input().split())
    route[a-1].append(b-1)
    route[b-1].append(a-1)

queue= deque([(route[0],0)])
# print(queue)

def bfs(queue):
    while queue:
        next,before = queue.popleft()
        for i in next:
            if used[i] != False:
                continue
            used[i] = before+1
            queue.append((route[i], i))

bfs(queue)

for i, v in enumerate(used):
    if i == 0:
        print("Yes")
    else:
        print(v)
# print(used)