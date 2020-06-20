N = int(input())
A = [int(input()) for _ in range(N)]


ans = 0
cnt = 0
for i in range(N):
    if A[i] != 0:
        ans += (A[i]+cnt)//2
        cnt = (A[i]+cnt)%2
    else:
        cnt = 0
print(ans)