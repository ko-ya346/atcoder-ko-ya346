def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
l = make_divisors(N)


ans = float("inf")
if len(l)%2:
    ans = l[len(l)//2]*2-2
else:
    for i in range(len(l)//2):
        ans = min(ans, l[i]-1+N//l[i]-1)
print(ans)