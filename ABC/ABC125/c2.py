from math import gcd

def init(init_val):
    for i in range(N):
        seg[i+num-1] = init_val[i]
    for i in range(num-2, -1, -1):
        seg[i] = gcd(seg[2*i+1], seg[2*i+2])

def update(k, x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = gcd(seg[k*2+1, seg[k*2+2]])

def query(p, q):
    if q <= p:
        return ide_ele
    p += num-1
    q += num-2
    res = ide_ele
    while q-p > 1:
        if p&1 == 0:
            res = gcd(res, seg[p])
        if q&1 == 1:
            res = gcd(res, seg[q])
            q -= 1
        p //= 2
        q = (q-1)//2
    if p == q:
        res = gcd(res, seg[p])
    else:
        res = gcd(gcd(res, seg[p]), seg[q])
    return res

N = int(input())
A = list(map(int, input().split()))

ide_ele = 0
num = 2**(N-1).bit_length()
seg = [ide_ele]*2*num

init(A)
ans = -1
for i in range(N):
    ans = max(ans, gcd(query(0, i), query(i+1, N)))
print(ans)