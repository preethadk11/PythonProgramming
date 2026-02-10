n=5
for i in range(1,n+1):
    for j in range((n-i)+1):
        print("*",end="")
    print(" ",end="")
    for s in range(2*i-2):
        print(" ",end="")
    print("*"*(n-i+1))
for i in range(n,0,-1):
    for j in range((n-i)+1):
        print("*",end="")
    print(" ",end="")
    for s in range(2*i-2):
        print(" ",end="")
    print("*"*(n-i+1))