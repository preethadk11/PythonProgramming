arr=[
    {"category":"fruit","name":"apple"},
    {"category":"fruit","name":"banana"},
    {"category":"vegetable","name":"carrot"}
]
this_dict={}
for obj in arr:
    category=obj["category"]
    if category not in this_dict:
        this_dict[category]=[]
    this_dict[category].append(obj)
print(this_dict)