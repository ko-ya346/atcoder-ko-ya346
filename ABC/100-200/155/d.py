N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

n = N-1
num = 0
while n < K:
    K -= n
    n -= 1
    num += 1
print(K)
print(num)
