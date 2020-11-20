N, X, Y = map(int, input().split())

l = [0 for _ in range(N)]
line = []

for i in range(1, N+1):
    for j in range(1, N+1):
        if i < j:
            l[min(abs(i-j), abs(X-i)+1+abs(Y-j), abs(X-j)+1+abs(Y-i))] += 1

for k in range(1, N):
    print(l[k])
