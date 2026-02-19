a=[[1,2,3],[4,5,6],[7,8,9]]
target=8
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==target:
            print(i,j)
            break