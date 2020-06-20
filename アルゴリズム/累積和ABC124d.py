n, k = map(int,input().split())
s = input()

t = 1
#連続した0と1の人をまとめる
l = [0]

for i in s:
    i = int(i)
    if i == t: 
        l[-1] += 1
    else: 
        l += [1]
        t = i

if t < 1: 
    l += [0]
# print(l)

#累積和をとる
s = [0]

for i in l:
    s += [s[-1]+i]

# print(s)

a = 0

for i in range(0,len(l),2):
    # print("i", i)
    # print("s[i+1]", s[i+1])
    # print("s[i-k*2]", s[i-k*2])
    if i<2*k:
        a = max(a, s[i+1])
    else:
        a = max(a, s[i+1]-s[i-k*2])
print(a) 
