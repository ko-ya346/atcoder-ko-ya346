import bisect

a = [1,1,2,3,3,4,4,4,5]

print(bisect.bisect(a, 2))
print(bisect.bisect_left(a, 2))
print(bisect.bisect_right(a, 2))