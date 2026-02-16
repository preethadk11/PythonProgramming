string=input()
non_repeating=""
for char in string:
    if string.count(char)==1:
        non_repeating=non_repeating+char
        break
print(non_repeating)