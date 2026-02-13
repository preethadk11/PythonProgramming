n=[5,3,8,1]
'''for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)'''
n.sort(reverse=True)
print(n)

'''number=sorted(n,reverse=True)
print(number)'''