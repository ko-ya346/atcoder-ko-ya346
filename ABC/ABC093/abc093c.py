a_s = list(map(int, input().split()))

count = 0
flag = 0

while flag == 0:
    if a_s[0] == a_s[1] and a_s[1] == a_s[2]:
        flag = 1
        break
    a_s = sorted(a_s)
    count += 1
    if a_s[2] > a_s[1] and a_s[2] > a_s[0]:
        a_s[0] += 1
        a_s[1] += 1
    else:
        a_s[0] += 2

print(count)
