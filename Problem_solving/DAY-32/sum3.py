import copy
data={
    "a":10,
    "b":[1,2,3]
}
shallow_copy=copy.copy(data)
print(id(data))
print(id(shallow_copy))