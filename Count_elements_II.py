n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
c=0
for i in a:
    if i not in b and i not in s:
        s.append(i)
        c+=1
for i in b:
    if i not in a and i not in s:
        s.append(i) 
        c+=1
print(c)        
        