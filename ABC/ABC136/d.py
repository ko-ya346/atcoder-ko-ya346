S = list(input())

ans = [0 for _ in range(len(S))]

s_flag = 0
cnt = 0
for i, s in enumerate(S):
    if s == "R":
        s_flag = 1
        cnt += 1
    else:
        if s_flag and s == "L":
            ans[i] += cnt//2 
            ans[i-1] += cnt//2 + cnt%2
            cnt = 0
            s_flag = 0
# print(ans)

S.reverse()
ans.reverse()
# print(S)
# print(ans)

l_flag = 0
cnt = 0
for i, s in enumerate(S):
    if s == "L":
        l_flag = 1
        cnt += 1
    else:
        if l_flag and s == "R":
            ans[i] += cnt//2 
            ans[i-1] += cnt//2 + cnt%2
            cnt = 0
            l_flag = 0
    # print(ans)
ans.reverse()
print(*ans)