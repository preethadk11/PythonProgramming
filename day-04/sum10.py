def leap_or_not(number):
    if number%4==0 and number%100!=0 or number%400==0:
        print("Leap year")
    else:
        print("Not leap year")
number=int(input("Enter a year: "))
leap_or_not(number)