str=input()
s=[]
for i in str:
    if i in 'aeiouAEIOU':
        if i not in s:
            s.append(i)
print(*s)            