n = int(input())
a = input()
al = list(map(int, a.split()))
ans = [al.index(i)+1 for i in al if i == 1]
all = set(al)
anss = []
print(ans)
if len(all) == 1 and al[0] == 0:
    print(0)
else:
    for i in ans:
        anss.append(i)
    if sum(al)%2 != al[0]:
        print(-1)
    else:
        for i in range(2,n):
            if sum(al[i::i])%2 != al[i]:
                print(-1)
                break
        else:
            print(sum(al))
            for i in len(ans):
                print(ans[i])
