n=int(input())
a=list(map(int,input().split()))
max=0
c=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c>max:
        max=c
        maxel=i
print(maxel,end=' ')        
    