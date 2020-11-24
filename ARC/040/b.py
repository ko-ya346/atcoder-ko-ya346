n, r = map(int, input().split())
m = list(input())
ans = 0
i = 0
while list(set(m)) != ["o"]:
    if "." not in m[i+r:]:
        ans += 1
        break
    # print("i", i, ans)
    if m[i] == ".":
        m[i:i+r] = ["o"] * r
        ans += 1
    # print(m)
    # print(m[i+r:])
    i += 1
    ans += 1
    
print(ans)