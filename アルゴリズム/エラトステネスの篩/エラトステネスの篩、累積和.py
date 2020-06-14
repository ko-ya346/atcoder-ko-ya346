import sys
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

max_n = 10**5

primes = eratosthenes(max_n)
# print(primes)

a = [0] * (max_n+1)
for i in range(1, max_n + 1):
    if i in primes and (i+1)//2 in primes:
        a[i] = a[i-1] + 1
    else:
        a[i] = a[i-1]
print(a)

Q = int(sys.stdin.readline().strip())
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().strip().split())
    print(a[r] - a[l-1])
