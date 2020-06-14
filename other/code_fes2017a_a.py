n, m, k = map(int, input().split())

# if n*m%2 == 0:
#     if k%2 == 0 and k >= min(n, m):
#         ans = 1
#     else:
#         ans = 0
# else:
#     ans = 1

# if ans:
#     print("Yes")
# else:
#     print("No")

n,m,K=map(int,input().split());print("YNeos"[all(k*m-K+l*n-k*l*2for k in range(n+1)for l in range(m+1))::2])
