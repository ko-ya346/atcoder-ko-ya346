N = int(input())
even = 0
A = []

for i in range(N):
    a = int(input())
    if not a%2:
        even += 1
    A.append(a)

if N == 1:
    print("sfeicrosntd"[(A[0]%2)::2])
elif sum(A) == N:
    print("first")
else:
    if even == N:
        print("second")
    else:
        print("first")