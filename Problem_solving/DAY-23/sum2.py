n=[1,2,3,1,5]
left=0
right=len(n)-1
while left<right:
    n[left],n[right]=n[right],n[left]
    left+=1
    right-=1
print(n)
