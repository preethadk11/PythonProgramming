a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
rows=len(a)
cols=len(a[0])
result=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(a[i][j]+b[i][j])
    result.append(row)
for row in result:
    print(*row) #unpacking operator