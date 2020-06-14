S = list(input())
n = len(S)+1
a = [0 for _ in range(n)]

for i in range(n-1):
    if S[i] == "<":
        a[i+1] = max(a[i+1], a[i] + 1)

# print(S)
# print(a)
S = S[::-1]
a = a[::-1]
for i in range(n-1):
    if S[i] == "<":
        S[i] = ">"
    else:
        S[i] = "<"

# print("".join(S))
# print(a)
for i in range(n-1):
    if S[i] == "<":
        if a[i] >= a[i+1]:
            a[i+1] = max(a[i+1], a[i] + 1)
# print(a)
print(sum(a))