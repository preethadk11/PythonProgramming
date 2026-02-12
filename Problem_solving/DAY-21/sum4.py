n=int(input())
sum=0
term=0
for i in range(1,n+1):
    term=term*10+1
    sum+=term
print(sum)