N = int(input())
S = input()

ans = S.count("R")*S.count("B")*S.count("G")
for i in range(N):
    #kとj、jとiの間をdとして表す
    for d in range(N):
        j = i+d
        k = j+d
        if k < N:
            if S[i] != S[j] and S[k] != S[j] and S[k] != S[i]:
                ans -= 1
print(ans)