this_list=["preetha","hello",12,32,12,"priyanga","preetha"]
counted=[]
for item in this_list:
    if item not in counted:
        count=this_list.count(item)
        print(item,":",count)
        counted.append(item)