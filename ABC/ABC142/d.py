from math import gcd

N, M = map(int, input().split())

n = gcd(N, M)
# print(n)

if n == 1:
    print(1)
else:
    ans = 1

    
    for i in range(2, int(gcd(N, M)**0.5)+1):
        flag = 0
        # print("i", i)
        # print("n", n)
        if n%i == 0:
            while n%i == 0:
                n //= i
                # print(n)
            flag = 1
        # print("n", n)
        ans += flag

    print(ans if n == 1 else ans+1)