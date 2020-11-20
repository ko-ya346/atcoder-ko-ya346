from collections import deque

N = int(input())

#頂点の色
path = [0 for _ in range(N-1)]
#木グラフ
tree = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append((b-1, i))
    # tree[b-1].append((a-1, i))
print(tree)

que = deque([])
que.append((0, 0))

while que:
    v, pc = que.popleft()
    c = 1
    for nv, i in tree[v]:
        print(f"nv{nv}, i{i}")
        if path[i] == 0:
            c = c+1 if c == pc else c
            path[i] = c
            que.append((nv, c))
            c += 1
    print("path", path)
    print("que", que)
print(max(path))
print(*path, sep="\n")

# import sys
# from collections import deque


# N = int(input())
# edge = [[] for _ in range(N)]
# for i in range(N-1):
#     a, b = map(int, input().split())
#     a -= 1; b -= 1
#     edge[a].append((b, i))
#     edge[b].append((a, i))

# path = [None] * (N - 1)
# q = deque()
# q.append((0, 0))

# while q:
#     v, pc = q.popleft()
#     c = 1
#     for nv, i in edge[v]:
#         if path[i] is None:
#             c = c + 1 if c == pc else c
#             path[i] = c
#             q.append((nv, c))
#             c += 1
#     print(q)

# '''deque([(1, 1)])
# deque([(2, 2), (3, 3), (4, 4)])
# deque([(3, 3), (4, 4)])
# deque([(4, 4), (6, 1)])
# deque([(6, 1), (5, 1)])
# deque([(5, 1)])
# deque([(7, 2)])
# deque([])'''

# print(max(path))
# print(*path, sep='\n')
