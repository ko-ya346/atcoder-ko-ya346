a, b, c, x, y = map(int, input().split())

n = min(x, y)
v1 = a * x + b * y
v2 = n * c * 2 + (x - n) * a + (y - n) * b
v3 = max(x, y) * c * 2
print(min(v1, v2, v3))