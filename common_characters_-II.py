s1=input().lower()
s2=input().lower()
#s1=s1.split()
#s2=s2.split()
c=0
k=[]
for i in s1:
    if i  in s2:
        k.append(i)
for i in s2:
    if i in s1:
        k.append(i)
for j in sorted(set(k))        :
    if j!=' ':
        c+=1
print(c)        
        