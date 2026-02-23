import copy
employee={
    "name":"John",
    "salary":[1000,2000]
}
shallow_copy=copy.copy(employee)
shallow_copy["name"]="Preetha"
shallow_copy["salary"][0]=67
print(employee)
print(shallow_copy)