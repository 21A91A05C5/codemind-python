a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
c=0
for i in l1:
    if i not in l2:
        s.append(i)
    if s.count(i)==1:
        c+=1
#print(c)    
for i in l2:
    if i not in l1:
        s.append(i)
    if s.count(i)    ==1:
        c+=1
print(c)        