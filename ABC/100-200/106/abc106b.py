s = input()
flag=1

cnt = 0
for i in s[2:-1]:
    if i == "C":
        cnt += 1
if s[0] != "A":
    flag = 0
else:
    if cnt != 1:
        flag = 0
    else:
        for i in range(len(s)):
            if s[i] == "A" or s[i] == "C":
                pass
            else:
                if s[i].isupper() == True:
                    flag = 0
if flag:
    print("AC")
else:
    print("WA")
