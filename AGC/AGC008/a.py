import numpy as np

xx, yy = map(int, input().split())

B = [(0, 0), (1, 0), (0, 1), (1, 1)]

ans = float("inf")
for i, j in B:
    x, y = xx, yy
    print(f"i, j, {i}{j}")
    if i:
        x *= -1
    if j:
        y *= -1
    if y >= x:
        ans = min(ans, y-x + i + j)
    print(ans)

print(ans)