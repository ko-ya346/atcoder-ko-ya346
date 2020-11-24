a, b, c = map(int, input().split())
max_ = max(a, b, c)
E = max_/(max_*3)*max_
sum_ = a+b+c

print((100-max_-a)*(max_-a)+(100-max_-b)*(max_-b)+(100-max_-c)*(max_-c))/sum_)