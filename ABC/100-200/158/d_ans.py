s = input()
q = int(input())
list1 = []
list2 = []
flag = 1
for i in range(q):
    in_line = input().split()
    if in_line[0] == "1":
        flag *= -1
    else:
        if in_line[1] == "1":
            if flag == 1:
                list1.append(in_line[2])
            else:
                list2.append(in_line[2])
        else:
            if flag == 1:
                list2.append(in_line[2])
            else:
                list1.append(in_line[2])
if flag == 1:
    print("".join(list1[::-1]) + s + "".join(list2))
else:
    print("".join(list2[::-1]) + s[::-1] + "".join(list1))