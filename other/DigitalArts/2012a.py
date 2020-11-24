S = input().split()
for _ in range(int(input())):
    t = input()
    for j in range(len(S)):
        s = S[j]
        lens = len(s)
        if len(t)!=lens:
            continue
        cnt = 0
        for i in range(lens):
            if t[i]=="*":
                cnt += 1
            elif s[i]==t[i]:
                cnt += 1
        if cnt == lens:
            S[j] = "*"*lens
print(" ".join(S))

