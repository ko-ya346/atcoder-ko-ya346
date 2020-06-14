N, Q = map(int, input().split())

follow = [["N" for _ in range(N)] for _ in range(N)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        follow[q[1]-1][q[2]-1] = "Y"
    
    elif q[0] == 2:
        for i in range(N):
            if follow[i][q[1]-1] == "Y":
                follow[q[1]-1][i] = "Y"

    else:
        copy = follow[q[1]-1].copy()
        for i, v in enumerate(copy):
            # print("i", i, "v", v)
            if v == "Y":
                for j in range(N):
                    # print(follow[i][j])
                    if follow[i][j] == "Y":
                        follow[q[1]-1][j] = "Y"
    # print(follow)

for i in range(N):
    follow[i][i] = "N"

    print("".join(follow[i]))
