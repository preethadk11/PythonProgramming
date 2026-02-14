n=[3,3,4,2,4,4,2,4,4]
candidate=None
count=0
for num in n:
    if count==0:
        candidate=num
    if num==candidate:
        count+=1
    else:
        count-=1
print(candidate)