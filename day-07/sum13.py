'''this_list=[
    {"name":"Preetha","marks":35},
    {"name":"Priyanga","marks":24}
]

avg=sum(item["marks"] for item in this_list)
print(avg/len(this_list))'''
this_list=[
    {"name":"Preetha","marks":35},
    {"name":"Priyanga","marks":24}
]
total=0
for item in this_list:
    total=total+item["marks"]
print(total/len(this_list))