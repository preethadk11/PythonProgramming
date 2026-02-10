n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print(" ",end="")
    for s in range(2*n-(2*i)):
        print(" ",end="")
    print("*"*i)

for i in range(n-1,0,-1):
    for j in range(1,i+1):
       print("*",end="")
    print(" ",end="")
    for s in range(2*n-(2*i)):
        print(" ",end="")
    print("*"*i)
    