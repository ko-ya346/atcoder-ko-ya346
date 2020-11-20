n = int(input())
c = input()

ans = 0
left = 0
right = n - 1

while left < right:
    # print(f"left: {left}")
    # print(f"right: {right}")
    # 一番左のW
    if c[left] == "R":
        left += 1
        continue
    # 一番右のR
    if c[right] == "W":
        right -= 1
        continue
    ans += 1
    left += 1
    right -= 1

print(ans)