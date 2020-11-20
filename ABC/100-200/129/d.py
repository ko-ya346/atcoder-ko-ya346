H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 0


for i in range(H):
    for j in range(W):
        # print(f"i{i} j{j}")
        cnt = 0
        if S[i][j] == ".":
            #右に進む
            for k in range(j+1, W):
                # print(f"rk{k}")
                if S[i][k] == "#":
                    # print("BBB")
                    break
                if k < W:
                    # print("c")                    
                    cnt += 1
            #左に進む
            for k in range(1, j+1):
                # print(f"lk{k}")
                if S[i][j-k] == "#":
                    # print("BBB")
                    break
                if k >= 0:
                    # print("c")
                    cnt += 1
            #下
            for k in range(i+1, H):
                # print(f"dk{k}")
                if S[k][j] == "#":
                    # print("BBB")
                    break
                if k < H:
                    # print("c")
                    cnt += 1
            #上
            for k in range(1, i+1):
                # print(f"uk{k}")
                if S[i-k][j] == "#":
                    # print("BBB")
                    break
                if k >= 0:
                    # print("c")
                    cnt += 1
        ans = max(ans, cnt+1)
        # print(f"ans{ans}--------------")
print(ans)