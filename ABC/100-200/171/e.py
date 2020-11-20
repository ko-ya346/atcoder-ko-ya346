N = int(input())
a = list(map(int, input().split()))

S = a[0]

for i in range(1, N):
    S ^= a[i]

ans = []
for i in a:
    ans.append(S^i)
print(*ans)
