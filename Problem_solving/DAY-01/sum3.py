'''number=input("Enter two numbers: ")
a,b=map(int,input().split())
a, b = map(int,number.split(" "))
if a>b:
    print("The larger number is: ",a)
print("The larger number is: ",b)
print("The larger number is: ",max(a,b))'''
num=input("Enter two numbers: ")
a,b=map(int,num.split(","))
print("The larger number is: ",max(a,b))