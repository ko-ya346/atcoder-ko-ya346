n, x = map(int, input().split())
ans = x
for s in input():
    if s=="x":
        ans = max(0, ans-1)
    else:
        ans += 1
print(ans)