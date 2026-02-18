import re
string=input()
letter=re.sub('[^a-zA-z]',"",string)
print(letter)