n, k, s = map(int, input().split())

if s == 10**9:
    a = 1
else:
    a = s+1
print((str(s)+" ")*k +(str(a)+" ")*(n-k))