# import sympy

# a, b, c = map(int, input().split())
# if  sympy.sqrt(a)+sympy.sqrt(b) < sympy.sqrt(c):
#     print("Yes")
# else:
#     print("No"


a, b, c = map(int, input().split())

if 4*a*b < (c-a-b)**2:
    print("Yes")
else:
    print("No")