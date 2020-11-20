from itertools import accumulate

N, M, K = map(int, input().split())
A = list(accumulate([0] + list(map(int, input().split()))))
B = list(accumulate([0] + list(map(int, input().split()))))


ans, j = 0, M

for i in range(N+1):
    if A[i] > K:
        break
    while B[j] > K-A[i]:
        j -= 1
    ans = max(ans, i+j)


print(ans)