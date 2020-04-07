s = input()
cardlist = [[i for i in range(1,9)], [1,2,3,4,9,10,11,12], \
    [1,2,5,6,9,10,13,14], [i for i in range(16) if i%2 == 1]]
ans = [True for i in range(17)]

for i in range(len(s)):
    if s[i] == "Y":
        for j in range(17):
            if j not in cardlist[i]:
                ans[j] = False
    else:
        for j in range(17):
            if j in cardlist[i]:
                ans[j] = False

for i in range(1, len(ans)):
    if ans[i]:
        print(i)
        break