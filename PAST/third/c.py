from math import log10

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x

A, R, N = map(int, input().split())

if N == 1 or R == 1:
    print(A)
else:
    if log10(R) > (log10(1000000000/A) / (N-1)):
        print("large")
    else:
        print(A * pow_k(R, N-1))