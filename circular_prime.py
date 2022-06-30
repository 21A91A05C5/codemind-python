def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
rev=0
if isprime(n):
    while(n):
        d=n%10
        rev=rev*10+d
        n=n//10
    if isprime(rev):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')