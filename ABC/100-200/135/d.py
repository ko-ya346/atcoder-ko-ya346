S = input()
n = len(S)

ans = 0
def dfs(cnt, mod):
    global ans

    if cnt >= n:
        if mod % 13 == 5:
            ans += 1
            ans %= 10 ** 9 + 7
        return
    else:
        s = S[cnt]
        keta = n - cnt - 1
        if s != "?":
            mod = (mod + int(s) * 10**keta) % 13
            dfs(cnt + 1, mod)
        else:
            for i in range(0, 10):
                mod = (mod + i * 10**keta) % 13
                dfs(cnt + 1, mod)

dfs(0, 0)
print(ans % (10 ** 9 + 7))