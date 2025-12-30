'''this_string=["preetha","hello"]
unique=set(this_string[0]).intersection(set(this_string[1]))
print(unique)'''
def func(this_list):
    common_chars=set(this_list[0])
    for i in range(0,len(this_list)):
            common_chars=common_chars.intersection(set(this_list[i]))
    return common_chars
this_list=["preetha","priyanga"]
print(func(this_list))