from collections import defaultdict
from bisect import bisect_left

S = input()
T = input()
ls = len(S)
idx = defaultdict(list)

for i, s in enumerate(S):
    idx[s].append(i)    

x = -1
for t in T:
    arr = idx[t]
    if len(arr) == 0:
        x = -2
        break
    y = (x+1) % ls
    i = bisect_left(arr, y)
    if i < len(arr):
        next_x = (x+1) + arr[i] - y
    else:
        next_x = (x+1) + arr[0] - y + ls
    x = next_x

print(x+1)