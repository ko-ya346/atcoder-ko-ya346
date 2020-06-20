X = list(input())

cnt = 0
s = 0
for i in range(len(X)):
    if X[i] == "S":
        s += 1
    else:
        if s:
            cnt += 2
            s -= 1
print(len(X)-cnt)