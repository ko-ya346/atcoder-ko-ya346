def f(a, b):
    if b:
        return f(b, a%b)
    return a

N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    print("POSSIBLE" if K==A[0] else "IMPOSSIBLE")
    exit()

p = f(A[0], A[1])

for i in A[1:]:
    p = f(p, i)

print("POSSIBLE" if p==f(p, K) and K <= max(A) else "IMPOSSIBLE")