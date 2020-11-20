N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
count = [0]*N

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

for _ in range(Q):
    p, x = map(int, input().split())
    count[p-1] += x

not_yet = [1]*N
not_yet[0] = 0
stack = [0]

while stack:
    parent = stack.pop()
    # print(parent)
    
    for child in edges[parent]:
        if not_yet[child]:
            count[child] += count[parent]
            not_yet[child] = 0
            stack.append(child)

print(*count)