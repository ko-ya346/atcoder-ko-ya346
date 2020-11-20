n,k = list(map(int,input().split()))
l = list(map(int,input().split()))

ans = []
for i in range(n-k+1):
    ans.append(min(abs(l[i]),abs(l[i+k-1]))+abs(l[i]-l[i+k-1]))
print(min(ans))