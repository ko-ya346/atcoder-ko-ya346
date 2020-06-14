N = int(input())
P = list(map(int, input().split()))

check = [0 for _ in range(N)]
ans = 0

for i, v in enumerate(P):
    if i+1 == v:
        check[i] = 1

for i in range(N-1):
    if check[i] == 1:
        ans += 1
        if check[i+1] == 1:
            check[i+1] = 0

print(ans + check[-1])