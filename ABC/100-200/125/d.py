N = int(input())
A = list(map(int, input().split()))

cnt = 0
f = 0

for i in range(N):
    if A[i] < 0:
        cnt += 1
        A[i] *= -1
    elif A[i] == 0:
        f = 1

# print(cnt)
# print(min(A))
# print(sum(A))
if cnt%2 == 0 or f:
    print(sum(A))
else:
    print(sum(A) - min(A)*2)