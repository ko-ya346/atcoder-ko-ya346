# K, N = map(int, input().split())
# a = list(map(int, input().split()))

# N = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    return gcd(r, b)

K = int(input())

ans = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        flag = 0
        n = gcd(a, b)
        if n == 1:
            flag = 1
        for c in range(1, K+1):
            if flag:
                ans += 1
            else:
                ans += gcd(n, c)

print(ans)