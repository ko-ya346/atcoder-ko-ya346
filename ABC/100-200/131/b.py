n, l = map(int, input().split())

apple = [l+i for i in range(n)]
abs_a = [abs(l+i) for i in range(n)]
print(sum(apple)-apple[abs_a.index(min(abs_a))])