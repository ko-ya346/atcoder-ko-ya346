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
    return Counter(a)

N = int(input())
a = list(map(int, input().split()))

ans = 0

for i in a:
    ans += prime_factorize(i)[2]
print(ans)