N, K = map(int, input().split())

if K%3 == 0:
    ans = N//K
else:
    ans = N//K*3
print(ans)