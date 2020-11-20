n = int(input())
s = input()

need_left = 0
pointer = 0

for i in range(n):
    if s[i] == "(":
        pointer += 1
    else:
        if pointer == 0:
            need_left += 1
        else:
            pointer -= 1

res = ""
for i in range(need_left):
    res += "("
res += s

for i in range(pointer):
    res += ")"

print(res)