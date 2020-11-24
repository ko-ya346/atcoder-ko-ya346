n, l = map(int, input().split())
amida = [" "+input()[1::2]+" " for _ in range(l)]
col = input()[::2].index("o")+1
for a in amida[::-1]:
    if a[col-1]=="-":
        col -= 1
    elif a[col]=="-":
        col += 1
print(col)