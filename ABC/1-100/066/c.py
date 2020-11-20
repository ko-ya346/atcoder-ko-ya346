from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = deque([])
for i in range(n):
    num = a[i]
    if i%2:
        b.appendleft(num)
    else:
        b.append(num)
    # b.reverse()
if n%2:
    b.reverse()
print(*b)