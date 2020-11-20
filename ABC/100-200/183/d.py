N, W = map(int, input().split())

total = [0 for _ in range(2*10**5+1)]

for _ in range(N):
    s, t, p = list(map(int, input().split()))
    total[s] += p
    if t < N:
        total[t] -= p

flag = 1
for i in range(N):
    if total[i] > W:
        flag = 0
        break
    total[i+1] += total[i]
# print(total)
if flag:
    print("Yes")
else:
    print("No")    