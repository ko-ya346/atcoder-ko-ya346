A, B, C, K = map(int, input().split())
if K%2:
    ans = -1*(A-B)
else:
    ans = A-B

if ans > 1000000000000000000:
    print("Unfair")
else:
    print(ans)