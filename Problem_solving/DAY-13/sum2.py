a=4
b=6
num1=a
num2=b
while(num2 != 0):
    r=num1%num2
    num1=num2
    num2=r
gcd=num1
lcm=(a*b)//gcd
print(lcm)
