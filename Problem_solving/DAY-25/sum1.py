this_list=[1,2,2,3,1,4,5,1]
this_dict={}
for i in this_list:
    if i not in this_dict:
        this_dict[i]=1
    else:
        this_dict[i]+=1
print(this_dict)