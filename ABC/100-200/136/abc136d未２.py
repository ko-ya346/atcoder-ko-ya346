s = input()
ans = [0 for i in range(len(s))]
RL_ind = []

for i in range(len(s)-2):
    if s[i:i+2] == "RL":
        RL_ind.append(i)
if s[-2:] == "RL":
    RL_ind.append(len(s)-2)

for i in range(len(s)):
    if s[i] == "R":
        ans_R = [j for j in RL_ind if j >= i]
        if (min(ans_R)-i)%2 == 0:
            ans[min(ans_R)] += 1
        else:
            ans[min(ans_R)+1] += 1
    else:
        ans_L = [j for j in RL_ind if j < i]
        if (max(ans_L)-i)%2 == 0:
            ans[max(ans_L)] += 1
        else:
            ans[max(ans_L)+1] += 1

print(*ans)