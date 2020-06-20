S = list(input())
K = int(input())

S1 = list(S)
cnt1 = 0
for i in range(1, len(S1)):
    if S1[i] == S1[i - 1]:
        S1[i] = '*'
        cnt1 += 1

S2 = list(S) * 2
cnt2 = 0
for i in range(1, len(S2)):
    if S2[i] == S2[i - 1]:
        S2[i] = '*'
        cnt2 += 1
        
S3 = list(S) * 3
cnt3 = 0
for i in range(1, len(S3)):
    if S3[i] == S3[i - 1]:
        S3[i] = '*'
        cnt3 += 1

# print("#", S1, S2, S3)
# print("#", cnt1, cnt2, cnt3)
ans = cnt1 + (cnt2 - cnt1) * (K // 2) + (cnt3 - cnt2) * ((K - 1) // 2)
print(ans)
