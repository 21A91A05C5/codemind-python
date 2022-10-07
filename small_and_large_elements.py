s=list(map(str,input().split()))
for i in s:
    i.lower()
    r=min(i)
    break
for i in s:
    p=max(i)
print(r,p,end=' ')    