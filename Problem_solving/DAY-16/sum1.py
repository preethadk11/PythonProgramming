num=int(input("Enter a number: "))
n=num
digit=0
while n>0:
    rem=n%10
    digit=digit*10+rem
    n=n//10
if num==digit:
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')

