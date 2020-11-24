a, b, c = map(int, input().split())

n1 = a*b*(c-c//2)- a*b*(c//2)
n2 = c*b*(a-a//2)- c*b*(a//2)
n3 = a*c*(b-b//2)- a*c*(b//2)

print(min(n1, n2, n3))