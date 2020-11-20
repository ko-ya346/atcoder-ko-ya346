n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = graph[y-1][x-1] = 1
ans = 0

for bit in range(1 << n):
    f = True
    # print(bin(bit))
    for j in range(n):
        for k in range(j):
            # print(f"j: {j}, k: {k}")
            if bit >> j & bit >> k & 1 and not graph[j][k]:
                f = False
    # print(f)
    if f:
        ans = max(ans, bin(bit).count("1"))
print(ans)