def check(s1, s2):
     
    # the sorted strings are checked
    if( len(s1)==len(s2)):
        ss=sorted(s1)
        rr=sorted(s2)
        if ss==rr:
            print("True")
        else:
            print("False")
    else:
        print("False")
# driver code 
s1 =input()
s1=s1.lower()
s2 =input()
s2=s2.lower()
check(s1, s2)