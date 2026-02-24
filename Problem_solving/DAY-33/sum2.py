def power(base,exp):
    if exp==0:
        return 1
    else:
        return base*power(base,exp-1)
base,exp=map(int,input("Enter base and exp: ").split())
print(power(base,exp))
