n=[0,1,2,0,3,4,0]
left=0
for i in range(len(n)):
    if n[i]!=0:
        n[left],n[i]=n[i],n[left]
        left+=1
print(n)