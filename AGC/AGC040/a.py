S = input()

dai = 0
sho = 0
ans = 0

#<のときは0
if S[0] == "<":
    f = 0
else:
    f = 1

for s in S:
    if s == "<":
        dai += 1
        if f:
            ans += (sho+1)*sho//2
            f = 0
            sho = 0
    elif s == ">":
        sho += 1
        if not f:
            ans += (dai+1)*dai//2
            f = 1
            dai = 0
    print("f", f, "dai", dai, "sho", sho, "ans", ans)

print(ans + dai + sho)
