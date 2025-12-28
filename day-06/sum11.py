def func(list1,list2):
    new_list=set(list1).union(set(list2))
    print(list(new_list))
list1=[23,44,54,66]
list2=[23,3,44,66]
func(list1,list2)