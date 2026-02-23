def func(num):
    if num==0:
        return 0
    else:
        return num+func(num-1)
num=int(input("Enter a number: "))
print(func(num))