a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
for i in l1:
    if i not in l2:
        s.append(i)
for i in l2:
    if i not in l1:
        s.append(i)
print(*s)        