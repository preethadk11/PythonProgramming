def common(list1,list2):
       result = set(list1).intersection(set(list2))
       print(list(result))
list1=[12,3,45,67,23]
list2=[23,4,55,66,78]
common(list1,list2)