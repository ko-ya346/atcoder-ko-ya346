memo = {}
def rec(a, b, c):
    if a==100 or b==100 or c==100:
        return 0
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    
    pa = a/(a+b+c)*(rec(a+1, b, c)+1)
    pb = b/(a+b+c)*(rec(a, b+1, c)+1)
    pc = c/(a+b+c)*(rec(a, b, c+1)+1)
    memo[(a, b, c)] = pa+pb+pc
    return pa+pb+pc
a, b, c = map(int, input().split())
print(rec(a, b, c))