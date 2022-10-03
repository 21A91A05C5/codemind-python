n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
c=0
for i in l1:
    if i in l2 and i not in s:
        s.append(i)
#print(*s)
for j in s:
    c+=1
print(c)    