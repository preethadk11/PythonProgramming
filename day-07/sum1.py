'''my_family={
    "child1":{
        "name":"preetha",
        "year":2006
    },
    "child2":{
        "name":"priyanga",
        "year":2009
    }
}
print(my_family)'''
child1={
    "name":"preetha",
    "year":2006
}
child2={
    "name":"priyanga",
    "year":2009
}
my_family={
    "child1":child1,
    "child2":child2
}
print(my_family)
for x,obj in my_family.items():
    print(x)
    for y in obj.keys():
        print(y,":",obj[y])