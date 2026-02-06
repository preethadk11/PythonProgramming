num=153
n=num
sum=0
while(n>0):
    rem=n%10
    sum=sum+(rem**(len(str(num))))
    n=n//10
if sum==num:
    print("Armstrong number")
else:
    print("Not an armstrong nubmer")