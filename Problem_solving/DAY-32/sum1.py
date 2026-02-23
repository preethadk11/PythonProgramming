import copy
'''obj={
    "name":"John",
    "age":25,
    "city":"New york"
}'''
obj={
    "name":"John",
    "age":25,
    "city":["karaikal","Nedugadu","velankanni"]
}
shallow_copy=copy.copy(obj)
shallow_copy["city"][0]="thanjore"
shallow_copy["age"]=98
print(obj)
print(shallow_copy)