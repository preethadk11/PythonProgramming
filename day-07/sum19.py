string1='Jessa'
count=0
my_dict={}
for char in string1:
    if char not in my_dict:
        count=1
        my_dict[char]=count
    else:
        my_dict[char]=count+1
print(my_dict)