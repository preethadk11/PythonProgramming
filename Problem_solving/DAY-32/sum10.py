obj={
    "a":1,
    "b":{
        "c":2,
        "d":{
            "e":3
        }
    }
}
flattend={}
for key,value in obj.items():
    if isinstance(value,dict):
        for inner_key,inner_value in value.items():
            
            if isinstance(inner_value,dict):
                for inner_inner_key,inner_inner_value in inner_value.items():
                    inner_new_key=key+"_"+inner_key+"_"+inner_inner_key
                    flattend[inner_new_key]=inner_inner_value
            else:
                new_key=key+"_"+inner_key
                flattend[new_key]=inner_value
    else:
        flattend[key]=value
print(flattend)