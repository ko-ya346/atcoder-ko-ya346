H, W, m = map(int, input().split())
h = [0 for _ in range(300001)]
w = [0 for _ in range(300001)]
bomb = set()
for _ in range(m):
    x, y = map(int, input().split())
    h[x-1] += 1
    w[y-1] += 1
    bomb.add((x-1, y-1))
mh = max(h)
mw = max(w)
ans = mh + mw

hi = [i for i, v in enumerate(h) if v == mh]
wi = [i for i, v in enumerate(w) if v == mw]

flag = 1
for i in hi:
    for j in wi:
        if (i, j) not in bomb:
            flag = 0
            break
    else:
        continue
    break

print(ans - flag)