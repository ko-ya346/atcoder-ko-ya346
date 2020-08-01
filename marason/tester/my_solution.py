D=int(input())
c=list(map(int,input().split()))
s=[]
for i in range(D):
    s.append(list(map(int,input().split())))

last=[0]*26
ans=0
for d in range(1,D+1):
    mx=-3650000
    mxt=-1

    for j in range(26):
        temp=last[j]
        last[j]=d
        score=0
        for i in range(26):
           score-=c[i]*(d-last[i])
        score+=s[d-1][j]

        if mx<score:
            mx=score
            mxt=j
        last[j]=temp
    last[mxt]=d

    print(mxt+1)



