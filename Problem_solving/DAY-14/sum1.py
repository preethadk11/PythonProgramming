value=int(input())
n=value
while(n>0):
    rem=n%10
    match rem:
        case 0:
            print("Zero",end=" ")
        case 1:
            print("One",end=" ")
        case 2:
            print("Two",end=" ")
        case 3:
            print("Three",end=" ")
        case 4:
            print("Four",end=" ")
        case 5:
            print("Five",end=" ")
        case 6:
            print("Six",end=" ")
        case 7:
            print("Seven",end=" ")
        case 8:
            print("Eight",end=" ")
        case 9:
            print("Nine",end=" ")
    
    n=n//10
