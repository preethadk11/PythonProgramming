base,exp=map(int,input("Enter base and exponent: ").split())
result=1
for i in range(exp):
    result=result*base
print(result)