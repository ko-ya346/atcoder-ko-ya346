from itertools import permutations

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

N, M, R = map(int, input().split())
r = list(map(int, input().split()))

road = [[float("inf")]*N for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    road[a-1][b-1] = c
    road[b-1][a-1] = c

for j in range(N):
    road[j][j] = 0

road = warshall_floyd(road)

# print(road)
ans = float("inf")

for v in permutations(r, len(r)):
    # print("v", v)
    tmp = 0
    for i in range(len(r)-1):
        tmp += road[v[i]-1][v[i+1]-1]
    # print(tmp)
    ans = min(ans, tmp)

print(ans)