base,exp=map(int,input("Enter base and exponent: ").split())
i=0
result=1
while(i<exp):
    result=result*base
    i+=1
print(result)