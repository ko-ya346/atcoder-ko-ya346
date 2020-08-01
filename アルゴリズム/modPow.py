def modPow(a, n, p):
    '''
    a**n mod p
    '''
    if n == 0:
        return 1
    elif n == 1:
        return a%p
    elif n%2 == 1:
        return (a*modPow(a, n-1, p))%p
    t = modPow(a, n//2, p)
    return (t**2)%p

a = 10**7
n = 10**7
p = 10**9+7
print(modPow(a, n, p))
#pythonの組み込み関数のpowも同じ
print(pow(a, n, p))