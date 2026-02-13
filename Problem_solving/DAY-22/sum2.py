max_count=0
count=0
result=[]
a=[1,2,3,3]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count+=1
        if count>max_count:
            max_count=count
            result.append(a[i])
print(result)