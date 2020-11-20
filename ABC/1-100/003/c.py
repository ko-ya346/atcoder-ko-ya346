N, K = map(int, input().split())
R = sorted(list(map(int, input().split())))

ans = 0
for i in range(N-K, N):
    ans = (ans+R[i])/2
print(ans)