N  = int(input())

ans = 0
G = []

for i in range(1, N):
    g = []
    a = list(map(int, input().split()))
    # print(a)
    for j, v in enumerate(a):
        g.append((j+i, v))
    G.append(g)

G.append([])

for index, i in enumerate(G):
    for v, cost in i:
        if cost >= 0:
            ans += cost
            # print("i", i, "v", v, "cost", cost, "index", index)
            if index != N-1:
                for i2, (v2, cost2) in enumerate(G[v]):
                    # print("i2", i2, "v2", v2, "cost2", cost2)
                    if cost2 >= 0:
                        ans += cost2
                        G[v][i2] = (v2, 0)

print(ans)