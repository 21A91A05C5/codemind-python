str=input()
s=[]
s1=input()
c=0
for i in range(len(str)):
    if str[i]==s1:
        print("True")
        print(i)
        break
else:
    print("False")
             