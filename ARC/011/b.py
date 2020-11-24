n = int(input())
key = list("bcdfghjklmnpqrstvwxz")
val = [1, 1, 2, 4, 9, 8, 3, 8, 5, 7, 9, 7, 4, 0, 6, 3, 5, 2, 6, 0]
dic = dict(zip(key, val))

ans = []
for S in input().split():
    num = ""
    for s in str.lower(S):
        if s in key:
            num += str(dic[s])
    if num != "":
        ans.append(num)

print(" ".join(ans))