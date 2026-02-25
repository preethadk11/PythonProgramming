def sumofdigits(num):
    if num==0:
        return 0
    else:
        return (num%10) +sumofdigits(num//10)
num=int(input("Enter number: "))
print(sumofdigits(num))