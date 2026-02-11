n=5
size=2*n-1
for i in range(size):
    for j in range(size):
        val =n - min(i,j,size-i-1,size-j-1)
        print(val,end=" ")
    print()