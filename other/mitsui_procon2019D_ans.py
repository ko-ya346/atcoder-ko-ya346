import sys
sys.setrecursionlimit(10**9)

N = int(input())
S = input()

num = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            num.append("{}{}{}".format(i, j, k))

ans = 0
for n in num:
    i = 0
    j = 0
    while j < N:
        # print(i, j)
        if n[i] == S[j]:
            i += 1
            j += 1
        else:
            j += 1
        if i == 3:
            ans += 1
            break
print(ans)
