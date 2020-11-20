from math import gcd

N = int(input())
A = list(map(int, input().split()))

L = [0] * N
L[0] = A[0]

#配列の左から順番に最大公約数を求める
for i, a in enumerate(A):
    L[i] = gcd(L[max(0, i-1)], a)

# print("L", L)
R = [0] * N
R[0] = A[-1]

#配列の右から順番に最大公約数を求める
for i, a in enumerate(A[::-1]):
    R[i] = gcd(R[max(0, i-1)], a)

# print("R", R)
ans = 0

for i in range(N):
    #一番左の数字を削除
    if i == 0:
        ans = max(ans, R[N-2])
    #一番右の数字を削除
    elif i == N-1:
        ans = max(ans, L[N-2])
    #i+1番目の数字を削除
    else:
        ans = max(ans, gcd(L[i-1], R[N-i-2]))
    
print(ans)
