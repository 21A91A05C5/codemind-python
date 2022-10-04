t=int(input())
for i in range(t):
    s=input()
    s.lower()
    res=s[::-1]
    if (res)==(s):
        if len(res)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")