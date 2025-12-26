number=int(input("Enter a number: "))
if number>=2:
    for i in range(2,(number-1)):
        if number%i==0:
            print("not prime")
            break
    else:
        print("prime")