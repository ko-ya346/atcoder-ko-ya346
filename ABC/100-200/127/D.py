N, M = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

card = [0] * M
for i in range(M):
    b, c = map(int, input().split())
    card[i] = (c, b)

card.sort(reverse=True)

arr = []
l = 0
#変更できるカード配列を作る
for i in range(M):
    if l+card[i][1] > 10**5:
        add = 10**5-l
        for j in range(add):
            arr.append(card[i][0])
        break
    else:
        for j in range(card[i][1]):
            arr.append(card[i][0])
        l += card[i][1]

a = a+arr
a.sort(reverse=True)
print(sum(a[:N]))