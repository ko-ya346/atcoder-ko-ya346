numR = int(input())
numB = int(input())
onlyR = int(input())
onlyB = int(input())
both = int(input())

n = numR*onlyR + numB*onlyB
ans = n

for _ in range(min(numR, numB)):
    n += both*2-onlyR-onlyB
    ans = max(ans, n)

print(ans)


'''
2
3
100
400
300

5
5
464
464
464

1
4
20
-30
-10

9
1
-1
-10
4
'''