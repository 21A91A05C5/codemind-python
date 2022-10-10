n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i not in s:
        s.append(i)
for i in s:
    print(i,end=' ')
    print(l.count(i),end=' ')
    