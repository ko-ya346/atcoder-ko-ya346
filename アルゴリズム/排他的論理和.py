N = int(input())
a = list(map(int, input().split()))

t = 0
for a_i in a:
    t ^= a_i
    # print(t)
print("Yes" if t==0 else "No")