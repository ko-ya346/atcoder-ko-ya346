N = int(input())
S = input()
ans = [-1 for _ in range(N+1)]

flag = 0
for i, s in enumerate(S[::2]):
    print(ans)
    i *= 2
    print(s, i)
    if ans[i] == -1:
        ans[i] = "S"
        if i+2 >= N:
            continue
        ans[i+2] = "WS"[s=="o"]
    else:
        if i+2 >= N:
            continue
        if s == "o":
            ans[i+2] = ans[i]
        else:
            ans[i+2] = "SW".replace(ans[i], "")
print("odd")
for i, s in enumerate(S[1::2]):
    print(ans)
    i = i*2 + 1
    print(s, i)
    if ans[i] == -1:
        ans[i] = "S"
        if i+2 >= N:
            continue
        ans[i+2] = "WS"[s=="o"]
    else:
        if i+2 >= N:
            continue
        if s == "o":
            ans[i+2] = ans[i]
        else:
            ans[i+2] = "SW".replace(ans[i], "")

print(ans)
