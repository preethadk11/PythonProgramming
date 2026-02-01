from collections import OrderedDict
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print(f'original dict:{my_dict}')
print('Sorted by values (as OrderedDict):')
values=OrderedDict(sorted(my_dict.items(),key=lambda x:x[1]))
print(values)