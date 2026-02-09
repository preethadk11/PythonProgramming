n=5
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    print("*",end="")
    if i>1 and i<5:
        for j in range(2*i - 3):
            print(" ",end="")
        print("*",end="")
    if i==n:
        for j in range(2*i - 2):
            print("*",end="")
    print()