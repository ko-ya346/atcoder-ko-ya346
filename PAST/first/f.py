S = input()

l = []
cnt = 0
word = ""

for s in S:
    if str.isupper(s):
        cnt += 1
    word += s
    if cnt == 2:
        l.append(word)
        word = ""
        cnt = 0
ans = sorted(l, key=str.lower)
# print(ans)
print("".join(ans))