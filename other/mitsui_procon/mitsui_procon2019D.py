N = int(input())
S = input()

l = []
ju = [0 for _ in range(len(S))]

def dfs(password, i):
    global l
    if len(password) == 3:
        l.append(password)
    ju[i] = 1
    password = password + S[i]
    print(password, i)
    for j in range(i+1, N-1):
        if i+j <= N and not ju[i+j]:
            dfs(password, i+j)

for i in range(N-2):
    password = ""
    dfs(password, i)
print(l)