from math import factorial

def comb(n, k, p):
    '''(nCk) mod oを求める'''
    if n<0 or k<0 or n<k:
        return 0
    if n == 0 or k == 0:
        return 1
    
    #n!, k!, (n-k)!をそれぞれ求める
    a = factorial(n)%p
    b = factorial(k)%p
    c = factorial(n-k)%p
    return (a*pow(b, p-2, p)*pow(c, p-2, p))%p

W, H = map(int, input().split())

mod = 10**9+7

print(comb(W+H-2, H-1, mod))