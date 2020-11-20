n, d = list(map(int, input().split()))
ans = n//(d*2+1)
if n%(d*2+1) == 0:
    print(ans)
else:
    print(ans+1)