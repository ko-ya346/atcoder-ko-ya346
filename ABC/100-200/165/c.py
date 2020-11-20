N, M, Q = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
for a in range(1, M+1):
    for b in range(a, M+1):
        for c in range(b, M+1):
            for d in range(c, M+1):
                for e in range(d, M+1):
                    for f in range(e, M+1):
                        for g in range(f, M+1):
                            for h in range(g, M+1):
                                for i in range(h, M+1):
                                    for j in range(i, M+1):
                                        tmp = 0
                                        MM = [a, b, c, d, e, f, g, h, i, j][:N]
                                        for ai, bi, ci, di in A:
                                            if MM[bi-1]-MM[ai-1] == ci:
                                                tmp += di
                                        ans = max(ans, tmp)
print(ans)

