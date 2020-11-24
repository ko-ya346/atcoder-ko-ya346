N = int(input())
c = input()
command = ["A", "B", "X", "Y"]

ans = float("inf")
for i in command:
    for j in command:
        for k in command:
            for l in command:
                L = i+j
                R = k+l
                if L==R:
                    continue
                tmp_c1 = c
                tmp_c2 = c

                if L in tmp_c1:
                    tmp_c1 = tmp_c1.replace(L, "L")
                if R in tmp_c1:
                    tmp_c1 = tmp_c1.replace(R, "R")
                if R in tmp_c2:
                    tmp_c2 = tmp_c2.replace(R, "R")
                if L in tmp_c2:
                    tmp_c2 = tmp_c2.replace(L, "L")
                ans = min(len(tmp_c2), len(tmp_c1), ans)

print(ans)