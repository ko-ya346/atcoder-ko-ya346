
'''
numの順番によっては買うことが出来ない金額が発生するためNG
num = [105, 104, 103, 102, 101, 100]

f = 0
for i in range(2**6):
    XX = X
    for j in range(6):
        if (i>>j)&1:
            XX %= num[j]
            if XX == 0:
                f = 1
print(f)
'''
X = int(input())
num = [105, 104, 103, 102, 101, 100]

dp = [0 for _ in range(X+1)]
dp[0] = 1
f = 1

for i in range(X+1):
    for j in num:
        if i-j >= 0:
            if dp[i-j]:
                dp[i] = 1

print(dp[X])