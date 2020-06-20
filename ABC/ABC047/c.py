S = list(input())

ans = 0
B = S[0] == "B"

for i in range(1, len(S)):
    if (S[i] == "B") != B:
        ans += 1
        B = S[i] == "B"
print(ans)
