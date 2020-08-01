N = int(input())
A = list(map(int, input().split()))

ans = 1
MOD = 1000000007
cnt = [0 for _ in range(N+1)]
cnt[0] += 3

for a in A:
    ans = ans*cnt[a]%MOD
    if ans == 0:
        break
    cnt[a] -= 1
    cnt[a+1] += 1
print(ans)
