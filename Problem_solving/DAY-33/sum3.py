def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
num=int(input())
for i in range(num):
    print(fib(i),end=" ")
