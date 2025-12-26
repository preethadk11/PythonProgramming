def palindrome(str):
    if str==str[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
string=input("Enter a string:").lower()
print(palindrome(string))