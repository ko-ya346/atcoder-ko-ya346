# S = input()

# n = len(S)
# ans = n
# ans2 = n

# for i in range(n-1):
#     if S[i] == "1":
#         ans = min(ans, max(n-i-1, i))
#     else:
#         ans2 = min(ans, max(n-i-1, i))


# print(max(ans, ans2))

S = input()

n = len(S)
ans = n

for i in range(n-1):
    if S[i] != S[i+1]:
        ans = min(ans, max(n-i-1, i+1))

S = S[::-1]
for i in range(n-1):
    if S[i] != S[i+1]:
        ans = min(ans, max(n-i-1, i+1))

print(ans)