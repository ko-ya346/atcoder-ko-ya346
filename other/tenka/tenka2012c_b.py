card = input()
mark = ["S", "H", "D", "C"]
royal = [[] for _ in range(4)]
print(card)
print(royal)

for i in range(len(card)):
    print(i)
    if i%2:
        continue
    print(mark.index(card[i]))
    royal[mark.index(card[i])].append(card[i+1])
print(royal)