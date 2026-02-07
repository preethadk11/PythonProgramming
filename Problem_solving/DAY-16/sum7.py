for i in range(1,5):
    for s in range(4-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(chr(64+j),end="")
    for j in range(2,i+1):
        print(chr(64+j),end="")
    print()

