from collections import Counter
n=int(input())
if n==1:
  print(1)
  exit()
xy=[tuple(map(int,input().split())) for _ in range(n)]

print(xy)
xy.sort()
print(xy)
l=[]
for i in range(n-1):
  for j in range(i+1,n):
    l.append((xy[j][0]-xy[i][0],xy[j][1]-xy[i][1]))
print(n-Counter(l).most_common()[0][1])
