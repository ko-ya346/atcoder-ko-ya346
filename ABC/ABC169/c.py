from decimal import *

A, B = input().split()
# print(int(Decimal(A)*Decimal(B)))
print(int(int(A) * int(float(B)*100)))