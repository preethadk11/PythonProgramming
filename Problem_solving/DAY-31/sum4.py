arr=[
    {"category":"fruit","name":"apple"},
    {"category":"fruit","name":"banana"},
    {"category":"vegetable","name":"carrot"}
]
result={}
for obj in arr:
    category=obj["category"]
    if category not in result:
        result[category]=[]
    result[category].append(obj)
print(result)