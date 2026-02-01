def func(inputdict):
    allvalues=list(inputdict.values())
    unique=set(allvalues)
    return len(allvalues)==len(unique)
    

dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}
print(f'Dictionary: {dict1}-> are all vaues unique? {func(dict1)}')
print(f'Dictionary: {dict2}-> are all vaues unique? {func(dict2)}')



