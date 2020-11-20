import numpy as np

H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
ans = []

for i, v in enumerate(a):
    for _ in range(v):
        ans.append(i+1)
ans = np.array(ans).reshape(H, W)

for i in range(H):
    if i%2 == 1:
        ans[i] = ans[i][::-1]

for j in ans:
    print(*list(j))