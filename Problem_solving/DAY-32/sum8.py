import copy
student={
    "name":"Preetha",
    "age":[34,5,6]
}
deep_copy=copy.deepcopy(student)
deep_copy["age"][0]=90
deep_copy["name"]="Priyanga"
student["name"]="John"
print(student)
print(deep_copy)