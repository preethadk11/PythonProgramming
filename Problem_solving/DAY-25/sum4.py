string="I love python and I love coding and I love learning".split()
this_list=string
this_dict={}
for i in this_list:
    if i not in this_dict:
        this_dict[i]=1
    else:
        this_dict[i]+=1
frequent=max(this_dict,key=this_dict.get)
print(frequent)
'''freak=max(this_dict.values())
for key in this_dict:
    if this_dict[key]==freak:
        print(key)'''