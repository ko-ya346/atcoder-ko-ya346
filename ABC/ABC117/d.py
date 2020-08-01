N, K = map(int, input().split())
A = list(map(int, input().split()))

xor = 0
for a in A:
    xor ^= a
if xor==0:
    xor = K

ans = 0
for a in A:
    ans += xor^a
print(ans)