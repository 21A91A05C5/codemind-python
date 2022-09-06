a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
for i in l1:
    if i not in l2:
        a.append(i)
for i in l2:
    if i not in l1:
        a.append(i)
print(*a,end=' ')
    