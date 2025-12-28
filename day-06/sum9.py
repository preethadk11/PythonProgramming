this_list=[23,"apple",12,"banana","apple"]
count=0
new_list=[]
for i in this_list:
    if i not in new_list:
        new_list.append(i)
        count=0
    elif i in new_list:
        count+=1
        print(i+":",count)