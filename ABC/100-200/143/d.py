from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
a.sort()

ans=0
print(a)
for i in range(1,n-1):
    for j in range(0,i):
        k=bisect_left(a,a[i]+a[j])-i-1
        print(f"i{i} j{j} bisect{bisect_left(a,a[i]+a[j])}")
        ans=ans+k
print(ans)
