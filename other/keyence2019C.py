N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

under = 0
over = []
cnt = 0

for i in range(N):
    if B[i] > A[i]:
        under += B[i] - A[i]
        cnt += 1
    elif B[i] < A[i]:
        over.append(A[i] - B[i])

over.sort(reverse=True)


# print("u", under)
# print("o", over)

for s in over:
    if under <= 0:
        break
    under -= s
    cnt += 1

if under <= 0:
    print(cnt)
else:
    print(-1)
