arr=[
    {"id":"a","value":1},
    {"id":"b","value":2},
    {"id":"c","value":3}
]
this_dict={obj["id"]:obj["value"] for obj in arr}
print(this_dict)