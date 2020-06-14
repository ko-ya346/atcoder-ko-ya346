N = int(input())

S = [[] for _ in range(N)]
for _ in range(5):
    s = input()[1:]
    ss = ""
    for i in range(4*N):
        if (i+1)%4:
            ss += s[i]
        else:
            S[(i+1)//4-1].append(ss)
            ss = ""

ans = ["-1" for _ in range(N)]

for i in range(N):
    if S[i][0][0] == ".":
        ans[i] = "1"
    elif S[i][0][1] == ".":
        ans[i] = "4"
    elif S[i][2][0] == S[i][2][1] == ".":
        ans[i] = "7"
    elif S[i][2][1] == ".":
        ans[i] = "0"
    elif S[i][3][2] == ".":
        ans[i] = "2"
    elif S[i][1][2] == "#" and S[i][1][0] == ".":
        ans[i] = "3"
    elif S[i][1][0] == "#" and S[i][1][2] == "." and S[i][3][0] == ".":
        ans[i] = "5"
    elif S[i][1][2] == ".":
        ans[i] = "6"
    elif S[i][3][0] == ".":
        ans[i] = "9"
    else:
        ans[i] = "8"

print("".join(ans))