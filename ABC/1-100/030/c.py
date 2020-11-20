from bisect import bisect_left

n, m = map(int, input().split())
x, y = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

time = {"a": a, "b": b}
key = "a"
now = 0
ans = 0

while True:
    index = bisect_left(time[key], now)

    if ((key == "a" and len(a) <= index) 
    or (key == "b" and len(b) <= index)):
        break
    
    if key == "a":
        now = a[index] + x
        key = "b"
    else:
        now = b[index] + y
        key = "a"

    ans += 1
    

print(ans//2)