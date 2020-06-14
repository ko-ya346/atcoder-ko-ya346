H, W = map(int, input().split())
if H%2 == 0 and W%2 == 0:
    print(H//2*W)
elif H%2 == 1 and W%2 == 0:
    print(W//2*H)
elif H%2 == 0 and W%2 == 1:
    print(H//2*W)
else:
    print(W//2*H+H//2+1)