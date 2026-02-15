string=input().lower()
reverse=""
for ch in string:
    reverse=ch+reverse
if reverse==string:
    print("Palindrome")
else:
    print("Not palindrome")