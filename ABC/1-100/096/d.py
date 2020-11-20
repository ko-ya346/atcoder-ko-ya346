import math

#必要な素数を全列挙
def eratosthenes(limit):
    A = [i for i in range(2, limit+1)]
    P = []
    time = 0

    while True:
        prime = min(A)

        if prime > math.sqrt(limit):
            break

        P.append(prime)

        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1

    for a in A:
        P.append(a)

    return set(P)

n = int(input())
primes = eratosthenes(55555)

ans = []

for p in primes:
    if len(ans) == n:
        break
    if p%5 == 4:
        ans.append(p)
print(*ans)
