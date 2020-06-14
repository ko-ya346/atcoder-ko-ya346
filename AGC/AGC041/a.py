n, a, b = map(int, input().split())

ans = float("inf")
if (b-a)%2:
    ans = min((b-a+1)//2+a-1, ans)
    ans = min((a+n-b+1)//2+n-b, ans)
else:
    ans = (b-a)//2
print(ans)