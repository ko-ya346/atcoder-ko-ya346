import numpy as np

n = int(input())
s = input()
s_W = [0]
s_E = []

for i in range(n):
    if s[i] == "W":
        s_W.append(1)
        s_E.append(0)
    else:
        s_W.append(0)
        s_E.append(1)

W_l = np.cumsum(np.array(s_W))
E_l = np.cumsum(np.array(s_E))

ans = []
for j in range(n):
    num = W_l[j]-W_l[0]+E_l[-1]-E_l[j]
    ans.append(num)
print(min(ans))