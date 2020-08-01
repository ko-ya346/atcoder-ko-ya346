from math import pi

l = sorted(list(map(int, input().split())), reverse=True)

s = (l[0]+l[1]+l[2])**2*pi
r = max(0, l[0]-l[1]-l[2])
print(s-r**2*pi)