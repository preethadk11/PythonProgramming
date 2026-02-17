string=input()
dup=[]
for char in string:
    if string.count(char)>1:
        if char not in dup:
            dup.append(char)
print(dup)