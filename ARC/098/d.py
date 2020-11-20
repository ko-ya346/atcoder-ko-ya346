N = int(input())
A = list(map(int, input().split()))

sumA = [0 for _ in range(N+1)]
xor = [0 for _ in range(N+1)]

for i in range(N):
    sumA[i+1] = sumA[i]+A[i]
    xor[i+1] = xor[i]^A[i]


