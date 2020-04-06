N, K, C = map(int, input().split())
S = input()

right, left = [0 for _ in range(N)], [0 for _ in range(N)]

cnt = 0
work = 0
while True:
    if work == K:
        break
    if S[cnt] != "x":
        right[cnt] += 1
        work += 1
        cnt += C+1
    else:
        cnt += 1

S = list(reversed(S))

cnt = 0
work = 0
while True:
    if work == K:
        break
    if S[cnt] != "x":
        left[cnt] += 1
        work += 1
        cnt += C+1
    else:
        cnt += 1

left.reverse()
# print(right)
# print(left)

cnt1 = 0
cnt2 = 0
for i in range(N):
    if right[i] == 1:
        cnt1 += 1
    if left[i] == 1:
        cnt2 += 1
    if right[i] == left[i] == 1 and cnt1 == cnt2:
        print(i+1)