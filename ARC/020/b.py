n, c = map(int, input().split())
A = [int(input()) for _ in range(n)]

ans = float("inf")
for i in range(1, 11):
    for j in range(1, 11):
        if i==j:
            continue
        cnt = 0
        for k, a in enumerate(A):
            if k%2:
                if j!=a:
                    cnt += 1
            else:
                if i!=a:
                    cnt += 1
        ans = min(ans, cnt)

print(ans*c)