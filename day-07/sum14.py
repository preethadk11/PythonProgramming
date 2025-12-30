this_string=input("Enter a string: ")
this_dict={}
count=1
for char in this_string:
    if char not in this_dict:
        
        this_dict[char]=1
    elif char in this_dict:
        this_dict[char]+=1
print(this_dict)
