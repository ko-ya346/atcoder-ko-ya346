N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A = sorted(AB[::2])
B = sorted(AB[1::2])

print(A)
print(B)
n = 1

if N%2 == 1:
    a, b = A[(N-1)//2]
    print(b-a+1)
else:
    a1, b1 = A[N//2]
    a2, b2 = A[N//2-1]
    if (b1-a1)%2 == 0 or (b2-a2)%2 == 0:
        n += 1
    print(b1-a1+b2-a2+n)