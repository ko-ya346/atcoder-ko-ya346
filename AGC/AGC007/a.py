H, W = map(int, input().split())
ans = 0
for _ in range(H):
    a = input()
    ans += a.count("#")
if ans == H+W-1:
    print("Possible")
else:
    print("Impossible")



#以下コードはWA
#離れた場所にある＃を認知できない

# grid = [list(input()) for _ in range(H)]

# sh, sw = 0, 0
# gh, gw = H-1, W-1
# move = [(1, 0), (0, 1)]

# f = 0
# queue= [[sh, sw]]
# # print(grid)

# if grid[0][0] == ".":
#     f = 1
# else:
#     while sh != gh or sw != gw:
#         sh, sw = queue.pop(0)
#         cnt = 0
#         for i, j in move:
#             if sh+i >= H or sw+j >= W:
#                 continue
#             if grid[sh+i][sw+j] == "#":
#                 if cnt:
#                     print("Impossible")
#                     exit()
#                 else:
#                     cnt += 1
#                     if sh+i == gh and sw+j == gw:
#                         print("Possible")
#                         exit()
#                     queue.append([sh+i, sw+j])
#         if not queue:
#             f = 1
#             break
# if f:
#     print("Impossible")