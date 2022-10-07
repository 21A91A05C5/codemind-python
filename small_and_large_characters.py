s=list(map(str,input().split()))
for i in s:
    i.lower()
    r=min(i)
    p=max(i)
    print(r,p,end=' ')    