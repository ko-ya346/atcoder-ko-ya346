N = int(input())
a = list(map(int, input().split()))
ans = 0
for i, v in enumerate(a):
    if (i+1)%2 and (v)%2:
        ans += 1
print(ans)
