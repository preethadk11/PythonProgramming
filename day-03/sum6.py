num=int(input("Enter a number: "))
if num<2:
    print("Not a prime")
else:
    for i in range(2,num-1):
        if num%i==0:
            print("Not a prime")
            break
    else:
        print("Prime")