N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

ans = 1
bus = 0
before = T[0]

for i in T:
    if bus+1 > C or i - before > K:
        bus = 1
        ans += 1
        before = i
    else:
        bus += 1
    
    # print(f"i{i} bus{bus} ans{ans}")
print(ans)
