data={
    "name":"John",
    "address":{
        "city":"chennai",
        "pincode":600001
    }
}
flattend={}
for key,value in data.items():
    if isinstance(value,dict):
        for inner_key,inner_value in value.items():
            new_key=key+"_"+inner_key
            flattend[new_key]=inner_value
    else:
        flattend[key]=value
print(flattend)