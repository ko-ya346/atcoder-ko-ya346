S = input()

if len(set(S)) == 1:
    print(0)
else:
    alpha = list(set(S))
    cnt = float("inf")
    for word in alpha:
        t = S[:]
        for i in range(1, len(S)):
            tmp = ""
            for j in range(len(t)-1):
                if t[j] == word or t[j+1] == word:
                    tmp += word
                else:
                    tmp += t[j]
            if len(set(tmp)) == 1:
                cnt = min(cnt, i)
                break
            t = tmp[:]
    print(cnt)