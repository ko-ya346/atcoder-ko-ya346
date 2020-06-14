N, M, Q = map(int, input().split())

solve = [[0 for _ in range(M+1)] for _ in range(N+1)]
m = [0 for _ in range(M+1)]

for _ in range(Q):
    s = list(map(int, input().split()))
    # print(s)
    if s[0] == 1:
        score = 0
        for i, f in enumerate(solve[s[1]]):
            if f:
                score += N-m[i]
        print(score)
    else:
        solve[s[1]][s[2]] = 1
        m[s[2]] += 1
        # print("s",solve)
        # print("m",m)