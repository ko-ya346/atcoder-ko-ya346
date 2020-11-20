n=int(input())
d=sorted([int(input()) for _ in range(n)])
sum_d=sum(d)
print(sum_d)
if n==1:
    print(sum_d)
else:
    print(max(0, d[-1]*2-sum_d))


