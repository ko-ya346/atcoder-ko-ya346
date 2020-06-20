from collections import Counter

def prime_factorize(n):
    a = 0
    while n % 2 == 0:
        a += 1
        n //= 2
    return a

N = int(input())
a = list(map(int, input().split()))

ans = 0

for i in a:
    ans += prime_factorize(i)
print(ans)