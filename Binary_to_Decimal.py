n=int(input())
for i in range(n):
    test_list=list(map(int,input().split()))
    res = int("".join(str(x) for x in test_list), 2)
    print( str(res))