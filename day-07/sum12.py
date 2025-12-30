def func(this_list):
    this_sorted=sorted(this_list,key=lambda x:x["marks"],reverse=True)
    return this_sorted
this_list=[
    {"name":"Preetha","marks":45},
    {"name":"Dhanya","marks":35},
    {"name":"Varanasi","marks":23}
]
print(func(this_list))