from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N, P = map(int, input().split())

l = Counter(prime_factorize(P))

ans = 1

for i, v in l.items():
    if v >= N:
        ans *= i**(v//N)
#     print(ans)
# print(l)
print(ans)
