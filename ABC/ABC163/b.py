N, M = map(int, input().split())
A = sum(list(map(int, input().split())))

if A<= N:
    print(N-A)
else:
    print(-1)