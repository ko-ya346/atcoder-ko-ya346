MARK = "SHDC"
NUM = "ATJQK"
card = input().replace("10", "T")
ans = []
cnt = [0 for _ in range(4)]

for i in range(len(card)):
    if i%2:
        continue
    if card[i+1] in NUM:
        ind = MARK.index(card[i])
        cnt[ind] += 1
        if cnt[ind] == 5:
            ans = [c for c in ans if (c[0]!=card[i]) or (c[1] not in NUM)]
            ans = "".join(ans).replace("T", "10")
            break
    ans.append(card[i:i+2])
            
if ans:
    print(ans)
else:
    print(0)