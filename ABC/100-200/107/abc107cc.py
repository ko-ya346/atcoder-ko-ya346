s = input()
ans = [0 for i in range(len(s))]
RL_ind = []
LR_ind = []

for i in range(len(s)-2):
    if s[i:i+2] == "LR":
        LR_ind.append(i)

for i in range(len(s)-2):
    if s[i:i+2] == "RL":
        RL_ind.append(i+1)
if s[-2:] == "RL":
    RL_ind.append(len(s)-1)
print(RL_ind)
print(LR_ind)

RL = 0
for i in range(len(s)):
    if i > LR_ind[RL]:
        RL += 1
    if (RL_ind[RL]-i)%2 == 0:
        ans[RL_ind[RL]] += 1
    else:
        ans[RL_ind[RL]-1] += 1
print(ans)