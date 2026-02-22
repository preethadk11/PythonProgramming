arr=[
    {"id":"a","value":1},
    {"id":"b","value":2},
    {"id":"c","value":3}
]
this_dict={}
for obj in arr:
    this_dict[obj["id"]]=obj["value"]
print(this_dict)