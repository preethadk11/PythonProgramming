import copy
person={
    "name":"john",
    "skills":["python","java"],
    "city":["chennai","delhi"]
}
shallow_copy=copy.copy(person)
shallow_copy["skills"][0]="c++"
print(shallow_copy)
print(person)