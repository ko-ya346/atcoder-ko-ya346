N = int(input())

s = sorted([input()[::-1] for _ in range(N)])
for i in s:
    print(i[::-1])