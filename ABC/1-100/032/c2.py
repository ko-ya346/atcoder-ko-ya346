N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
    exit()

ans = 0
tmp = 1
right = 0

for left in range(N):
    while right<N and tmp*s[right] <=K:
        tmp *= s[right]
        right += 1
    ans = max(ans, right-left)
    if right == left:
        right += 1
    else:
        tmp //= s[left]
print(ans)