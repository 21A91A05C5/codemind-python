s=list(map(str,input().split()))
c=0
for i in s:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    print(c,end=' ')            