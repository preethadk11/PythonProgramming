max_count=0
count=0
n=[1,1,0,1,1,1]
for i in n:
    if i==1:
        count+=1
        max_count=max(max_count,count)
    else:
        count=0
print(max_count)