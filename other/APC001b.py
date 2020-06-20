N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = 0, 0

for i in range(N):
    if A[i]>B[i]:
        b += A[i]-B[i] 
    elif A[i]<B[i]:
        a += (B[i]-A[i])/2

# print(f"a{a} b{b}")
# print(sum(B)-sum(A))

if a>=b:
    print("Yes")
else:
    print("No")