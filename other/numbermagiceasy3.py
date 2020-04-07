s = input()
string = ["YYYYYYYYNNNNNNNN","YYYYNNNNYYYYNNNN", \
    "YYNNYYNNYYNNYYNN", "YNYNYNYNYNYNYNYN"]
for i in range(16):
    temp = ""
    for j in range(4):
        temp += string[j][i]
    if s==temp:
        print(i+1)
        break