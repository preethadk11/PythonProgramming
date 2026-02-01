from collections import OrderedDict
my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

sorted_dict = OrderedDict(sorted(my_dict.items(),key=lambda x: x[1]))
print(sorted_dict)