a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
rows=len(a)
cols=len(a[0])
result=[[0,0],[0,0]]
for i in range(rows):
    for j in range(cols):
        for k in range(2):
            result[i][j]+=a[i][k]*b[k][j]
print(result)