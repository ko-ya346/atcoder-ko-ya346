def query(a,b,k,l,r):
    if r <= a or b <= l:
        return -float("inf")
    elif a <= l and r <= b:
        return seg[k]
    else:
        return max(query(a,b,2*k+1,l,(l+r)//2),query(a,b,2*k+2,(l+r)//2,r))