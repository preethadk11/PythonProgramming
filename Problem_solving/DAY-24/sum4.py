n=[0,1,2,0,3,4,0]
right=len(n)-1
i=0
while i<=right:
    if n[i]==0:
        n[i],n[right]=n[right],n[i]
        right-=1
    else:
        i+=1
print(n)