a, b = list(map(int,input().split()))
sum = 0
for i in range(1, b-a+1):
    sum += i
print(sum-b)