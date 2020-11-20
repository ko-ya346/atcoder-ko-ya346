H, W, K = map(int, input().split())

C = [list(input()) for _ in range(H)]

# hbit = [[0]*H for _ in range(2**H)]
# wbit = [[0]*W for _ in range(2**W)]

# for i in range(2**H):
#     for j in range(H):
#         if ((i >> j)&1):
#             hbit[i][j] = 1

# for i in range(2**W):
#     for j in range(W):
#         if ((i >> j)&1):
#             wbit[i][j] = 1

ans = 0
for ii in range(2**H):
    for jj in range(2**W):
        tmp = 0
        for i in range(H):
            for j in range(W):
                # print(ii>>i, jj>>j)
                if (ii>>i)&1 or (jj>>j)&1:
                    continue
                if C[i][j] =="#":
                    tmp += 1
        if tmp == K:
            ans += 1
print(ans)