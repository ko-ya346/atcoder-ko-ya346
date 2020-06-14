N, M, Q = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

c = list(map(int, input().split()))

for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        print("--------", c[s[1]-1])
        for i in G[s[1]-1]:
            c[i] = c[s[1]-1]
    else:
        print("--------",c[s[1]-1])
        c[s[1]-1] = s[2]