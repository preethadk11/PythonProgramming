this_list=[
    {"name":"Preetha","age":19,"marks":94},
    {"name":"Dhanya","age":18,"marks":90},
    {"name":"Priyanga","age":17,"marks":97}
]
highest=max(this_list,key=lambda x:x["marks"])
print(highest)
