list1=[12,3,45,66,76]
list2=[12,4,544,66]
new_list=[]
for i in list1:
    if i in list1 and i in list2:
        new_list.append(i)
print(new_list)