a, b = map(int, input().split())

if a <= 0 and b >= 0:
    ans = "Zero"
elif a > 0:
    ans = "Positive"
else:
    if (b-a)%2:
        ans = "Positive"
    else:
        ans = "Negative"
print(ans)