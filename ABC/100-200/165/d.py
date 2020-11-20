from math import floor

a, b, n = map(int, input().split())
# a, b, n = 10, 8, 10

num = min(b-1, n)
#n以下で最大のbの倍数
print(floor(a*num/b) - a*floor(num/b))



# ans = 0
# for i in range(1,100):
#     tmp = floor(a*i/b) - a*floor(i/b)
#     print("i", i, "tmp", tmp)
#     ans = max(ans, tmp)


# if a > b:
#     print(floor(a-a/b))
# elif a<b:
#     print(ceil(b/a))
# else:
#     print(a-1)