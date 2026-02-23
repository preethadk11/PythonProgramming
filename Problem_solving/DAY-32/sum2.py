'''import copy
student={
    "name":"john",
    "age":20
}
shallow=copy.copy(student)
print(shallow)
print(student)'''
import copy
student={
    "name":"John",
    "marks":[45,23,90]
}
shallow_copy=copy.copy(student)
shallow_copy["marks"][0]=100
print(student)
print(shallow_copy)