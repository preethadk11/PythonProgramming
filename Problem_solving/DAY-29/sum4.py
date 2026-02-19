a=[[1,2,3],[4,5,6]]
result=[]
for i in range(len(a[0])):
    row=[]
    for j in range(len(a)):
        row.append(a[j][i])
    result.append(row)
print(result)
        
