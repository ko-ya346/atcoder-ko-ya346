l,r =map(int, input().split())

if r-l >= 2019:
    print(0)
else:
    ll = []
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i == j:
                pass
            else:
                ll.append(i*j%2019)
    print(min(ll))            