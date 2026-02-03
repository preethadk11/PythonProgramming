n=8
for i in range(n):
    for j in range(i):
        print(" ",end="")
    print("*"*(2*n-(2*i+1)))
