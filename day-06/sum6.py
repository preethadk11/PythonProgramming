def square(this_list):
    new_list=[]
    for i in this_list:
        new_list.append(i*i)
    return new_list
this_list=[56,4,76,33,3,2]
print(square(this_list))