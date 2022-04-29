x=int(input())
y=int(input())
sum1=0
sum2=0
for i in range(1,x):
    if(x%i==0):
        sum1+=i
    if(y%i==0):
        sum2+=i
if(y==sum1 and x==sum2):
    print('Amicable')
else:
    print("Not Amicable")