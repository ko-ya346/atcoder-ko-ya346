n = int(input())
d = list(map(int, input().split()))

dd = sorted(d)
ans = 0

if dd[int(n/2)] != dd[int(n/2)-1]:
    ans += dd[int(n/2)]-dd[int(n/2)-1]

print(ans)
