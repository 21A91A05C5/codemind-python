t=int(input())
for i in range(t):
    n=input()
    c=0
    l=[]
    for i in n:
        l.append(int(i))
    a=max(l)    
    b=min(l)
    p=[]
    for j in range(b,a+1):
        p.append(j)
    if sorted(p)==sorted(l) :
        print("YES")
    else:
        print("NO")