# K, N = map(int, input().split())
# a = list(map(int, input().split()))

# N = int(input())

n = input()
flag = 0
for i in n:
    if i == "7":
        flag = 1
        break

if flag:
    print("Yes")
else:       
    print("No")
