# s = list(input())

# ans = 0
# f = 1

# while f:
#     tmp = s
#     f = 0
#     for i in range(len(s)-2):
#         if tmp[i:i+3] == ["A", "B", "C"]:
#             s[i:i+3] = ["B", "C", "A"]
#             ans += 1
#             f = 1

# print(ans)

s = input().replace("BC", "D")
a = 0
c = 0
for i in s[::-1]:
    if i == "D":
        c += 1
    elif i == "A":
        a += c
    else:
        c = 0
print(a)