import copy
employee={"x":[12,3,4]}
shallow_copy=copy.copy(employee)
shallow_copy["x"]=[12,22,3]
print(employee)
print(shallow_copy)