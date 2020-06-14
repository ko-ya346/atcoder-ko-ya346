H, W, A, B = map(int, input().split())

grid = [["0" for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if (i < B and j < A) or (i >= B and j >= A):
            grid[i][j] = "1"

for row in grid:
    print("".join(row))