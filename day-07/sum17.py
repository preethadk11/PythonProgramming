'''keys=['ten','twenty','thirty']
values=[10,20,30]
my_dict=dict(zip(keys,values))
print(my_dict)'''
keys=['ten','twenty','thirty']
values=[10,20,30]
res_dict=dict()

'''res_dict={}
for k,v in zip(keys,values):
    res_dict[k]=v
print(res_dict)'''
for i in range(len(keys)):
    res_dict.update({keys[i]:values[i]})
print(res_dict)
