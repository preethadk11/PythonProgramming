'''rows=5
columns=5
for i in range(1,5+1):
    for j in range(1,5+1):
        if i==1 or i==rows or j==1 or j==columns:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
rows=5
columns=6
for i in range(1,6):
    for j in range(1,7):
        if i==1 or i==rows or j==1 or j==columns:
            print("*",end="")
        else:
            print(" ",end="")
    print()