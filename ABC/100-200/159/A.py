import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, M = list(map(int, input().split()))

if N > 2:
    a = combinations_count(N, 2)
elif N == 2:
    a = 1
else:
    a = 0

if M > 2:
    b = combinations_count(M, 2)
elif M == 2:
    b = 1
else:
    b = 0

print(a+b)