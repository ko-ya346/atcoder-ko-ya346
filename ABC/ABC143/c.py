N = int(input())
S = input()

s = S[0]
cnt = 1

for i in range(1, N):
    if s != S[i]:
        cnt += 1
        s = S[i]
print(cnt)