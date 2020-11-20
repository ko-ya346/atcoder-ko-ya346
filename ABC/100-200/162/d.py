N = int(input())
S = input()

cnt = 0
l = ["R", "G", "B"]
for i in range(len(S)-2):
    for j in range(i, len(S)):
        if S[i] != S[j]:
            for k in range(j, len(S)):
                s = [S[i], S[j], S[k]]
                if set(s) == set(l):
                    if j-i != k-j:
                        cnt += 1
print(cnt)