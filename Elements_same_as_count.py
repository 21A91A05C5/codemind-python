n=int(input())
l=list(map(int,input().split()))
c=0
s=[]
k=[]
for i in l:
    if l.count(i)==i:
        s.append(i)
    if s.count(i)==1:
        k.append(i)
        c+=1
if c>0:
    print(*k,end=' ')
else:
    print("-1")