N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
a1 = sorted(a, key=(lambda x:x[1]))
a2 = sorted(a, key=(lambda x:x[1]), reverse=True)
a3 = sorted(a, key=(lambda x:x[0]))
a4 = sorted(a, key=(lambda x:x[0]),reverse=True)

cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
max_n1,max_n2,max_n3,max_n4 = sum(a1[0]),sum(a2[0]),sum(a3[0]),sum(a4[0])

for point, area in a1[1:]:
    i = point-area
    if max_n1 > i:
        cnt1 += 1
    else:
        max_n1 = point+area

for point, area in a2[1:]:
    i = point-area
    if max_n2 > i:
        cnt2 += 1
    else:
        max_n2 = point+area

for point, area in a3[1:]:
    i = point-area
    if max_n3 > i:
        cnt3 += 1
    else:
        max_n3 = point+area

for point, area in a4[1:]:
    i = point-area
    if max_n4 > i:
        cnt4 += 1
    else:
        max_n4 = point+area

print(max(N-cnt1,N-cnt2,N-cnt3,N-cnt4))