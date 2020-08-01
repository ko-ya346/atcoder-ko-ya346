N = int(input())
A = list(map(int, input().split()))

l = []
for i, a in enumerate(A):
    l.append((i+1, a))
l.sort(key=lambda x: x[1], reverse=True)

for i in range(N):
    print(l[i][0])