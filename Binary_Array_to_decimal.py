n=int(input())
test_list=list(map(int,input().split()))
# printing original list

 
# using join() + list comprehension
# converting binary list to integer
res = int("".join(str(x) for x in test_list), 2)
 
# printing result
print( str(res))