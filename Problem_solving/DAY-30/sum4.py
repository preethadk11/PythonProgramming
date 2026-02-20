obj={
    "name":"John",
    "age":25,
    "city":"New york"
}
'''swapped={value:key for key,value in obj.items()}
print(swapped)'''
swapped={}
for key,value in obj.items():
    swapped[value]=key
print(swapped)