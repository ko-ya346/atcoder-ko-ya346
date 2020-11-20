N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()

i = N//2
if N%2 == 0:
    print(B[i]+B[i-1]-A[i]-A[i-1]+1)
else:
    print(B[i]-A[i]+1)