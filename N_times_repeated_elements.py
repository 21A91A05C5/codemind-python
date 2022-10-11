n=int(input())
l=list(map(int,input().split()))
k=int(input())
b=[]
for i in l:
    c=0
    if l.count(i)==k:
        b.append(i)
    if b.count(i)==1:
        print(i,end=' ')
if b==[]:
    print("-1")