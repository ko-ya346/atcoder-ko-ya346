N = int(input())
A = list(map(int, input().split()))

ans = [0]*N

#TLE解
# for i in range(N):
#     if i%2 == 0:
#         ans[i] = sum(A[0:i:2])-sum(A[1:i:2])+A[i]+sum(A[i+1::2])-sum(A[i+2::2])
#     else:
#         ans[i] = -sum(A[0:i:2])+sum(A[1:i:2])+A[i]+sum(A[i+1::2])-sum(A[i+2::2])
# ans.insert(0, ans.pop(-1))

ans[0] = sum(A)-sum(A[1::2])*2
for i in range(1, N):
    ans[i] = A[i-1]*2-ans[i-1]
print(*ans)