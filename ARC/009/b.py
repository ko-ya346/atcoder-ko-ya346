b = input().split()
dic2 = dict(zip(list(map(str, range(10))), b))
dic = dict(zip(b, list(map(str, range(10)))))
n = int(input())
a = []
for _ in range(n):
    tmp = input().translate(str.maketrans(dic))
    a.append(int(tmp))
a.sort()
for aa in a:
    print(str(aa).translate(str.maketrans(dic2)))
