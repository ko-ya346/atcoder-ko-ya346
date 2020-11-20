from collections import Counter

N, K, Q = map(int, input().split())
a = [int(input()) for _ in range(Q)]

ju = [0 for _ in range(N)]

for i in range(Q):
    ju[a[i]-1] += 1

# print(ju)
for v in ju:
    if K-Q+v <= 0:
        print("No")
    else:
        print("Yes")