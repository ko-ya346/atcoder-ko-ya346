N, A, B = map(int, input().split())

if A == 0:
    ans = 0
if N%(A+B) > A:
    ans = N//(A+B)*A + A
else:
    ans = N//(A+B)*A + N%(A+B)

print(ans)