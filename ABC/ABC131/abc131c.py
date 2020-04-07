import math

list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(n)]


d_count = 0
cd_count = 0
for i in range(ac):
    c_count += 1
    if i*c > b:
        break

for i in range(ad):
    d_count += 1
    if i*d > b:
        break

for i in range(acd):
    cd_count += 1
    if i*acd > b:
        break

print(b-a-c_count-d_count+cd_count)