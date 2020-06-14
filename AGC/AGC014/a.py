a, b, c = map(int, input().split())

def f(a, b, c):
    if a%2==1 or b%2==1 or c%2==1:
        return 0
    if a==b==c:
        return -1
    return f((b+c)/2, (c+a)/2, (a+b)/2)+1
ans = f(a, b, c)
print(ans)