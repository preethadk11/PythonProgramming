number=int(input())
factor=[]
prime=[]
for i in range(2,number):
    if number%i==0:
        factor.append(i)
print(factor)
for i in factor:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.append(i)
print(max(prime))