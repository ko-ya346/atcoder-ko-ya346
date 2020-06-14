n, a, b = map(int, input().split())
mod = 10**9+7

def cmb(n, r):
    x, y = 1, 1
    for i in range(r):
        x = x*(n-i)%mod
        y = y*(i+1)%mod
    #フェルマーの小定理
    return x*pow(y, mod-2, mod)%mod

print((pow(2, n, mod)-cmb(n, a)-cmb(n, b)-1)%mod)