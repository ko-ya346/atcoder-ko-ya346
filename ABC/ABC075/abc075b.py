H,W = map(int,input().split())
src = [input() for i in range(H)]
 
ans = []
for row in src:
    ans.append(list(row))

print(ans)