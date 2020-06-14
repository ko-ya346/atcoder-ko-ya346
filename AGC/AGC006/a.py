n=int(input())
s=input()
t=input()
c=0
for i in range(n):
    print(s[-i-1:])
    print(t[:i+1])
    if s[-i-1:]==t[:i+1]:
        c=i+1
print(n*2-c)
