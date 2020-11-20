# 縦横の制約を満たせない
a, b = map(int, input().split())

grid1 = ["w" if i%2 else "b" for i in range(max(a, b)*2)]
if (a+b)%2==0:
    grid1.append("w")

if abs(a-b) != 0:
    grid2 = ["w" for _ in range(len(grid1))]
    for i in range(max(a, b)-abs(a-b)-1):
        grid2[i*2+2] = "b"

    ans = [grid1, grid2]
    print(2, len(grid1))
    for grid in ans:
        if a < b:
            print("".join(grid).replace("b", "#").replace("w", "."))
        else:
            print("".join(grid).replace("b", ".").replace("w", "#"))
else:
    print(1, len(grid1)-1)
    print("".join(grid1[:-1]).replace("b", ".").replace("w", "#"))