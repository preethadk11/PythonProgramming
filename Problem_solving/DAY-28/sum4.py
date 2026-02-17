a=[[2,4],[6,8]]
b=[[1,3],[5,7]]
rows=len(a)
cols=len(a[0])

result=[]
for i in range(rows):
  row=[]
  for j in range(cols):
    row.append(a[i][j]+b[i][j])
  result.append(row)
print(result)
