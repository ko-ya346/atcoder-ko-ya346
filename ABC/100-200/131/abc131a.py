n = input()
flag = 0
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        flag = 1

if flag == 1:
    print("Bad")
else:
    print("Good")