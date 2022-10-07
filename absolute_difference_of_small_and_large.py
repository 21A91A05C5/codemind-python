s=list(map(str,input().split()))
for i in s:
    r=ord(min(i))
    p=ord(max(i))
    print(p-r,end=' ')