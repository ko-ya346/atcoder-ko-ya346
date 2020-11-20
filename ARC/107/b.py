n, k = map(lambda x:abs(int(x)), input().split())

ans = 0
for ab in range(2, 2*n+1):
    cd = ab-k
    if 2<=cd<=2*n:
        ans += min(ab-1, 2*n+1-ab) * min(cd-1, 2*n+1-cd)
print(ans)