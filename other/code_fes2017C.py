s = input()

ans = 0

l, r = 0, len(s)-1
if len(s) != 1:
    while l != r:
        print("l", l, "r", r)
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if s[l] == "x":
                l += 1
                ans += 1
            elif s[r] == "x":
                r -= 1
                ans += 1
            else:
                ans = -1
                break

print(ans)