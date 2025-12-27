terms=int(input("Enter number of terms:"))
fib=[0,1]
for i in range(2,terms):
    fib.append(fib[-1]+fib[-2])
print(fib)