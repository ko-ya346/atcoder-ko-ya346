s = input()
t = input()

sl = {}
tl = {}

for i, j in zip(s, t):
    if i not in sl:
        sl[i] = j
    else:
        if sl[i] != j:
            print("No")
            break
    if j not in tl:
        tl[j] = i
    else:
        if tl[j] != i:
            print("No")
            break
else:
    print("Yes")