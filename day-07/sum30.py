original_dict1 = {'a': 1, 'b': 2, 'c': 3}
another={}
for key,value in original_dict1.items():
    another[value]=key
print(another)