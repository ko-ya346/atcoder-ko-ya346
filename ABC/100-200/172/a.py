N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

time = 0
cnt = 0
b = []

for i in range(M):
    if time+B[i] > K:
        break
    b.append(B[i])
    time += B[i]
    cnt += 1

ai, bi = 0, 0
b.reverse()

while True:
    if time + A[0] < K:
        cnt += 1
        time += A.pop(0)
    if A[0] > b[0]

print(b)

print(cnt)