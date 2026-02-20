obj={
    "name":"John",
    "age":25,
    "city":"New york"
}
this_dict={}
for key,value in obj.items():
    temp=key
    key=value
    value=temp
    this_dict[key]=value
print(this_dict)
    