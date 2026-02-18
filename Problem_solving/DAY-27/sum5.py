string=input()
result=""
for char in string:
    if char.isalpha():
        result+=char
print(result)