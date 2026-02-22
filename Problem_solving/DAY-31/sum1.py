obj1={
    "a":1,
    "b":2,
    "c":1
}
obj2={
    "a":1,
    "b":2,
    "c":3
}

if len(obj1)!=len(obj2):
    print("Not same")
else:
    flag=True
    for key in obj1:
        if key not in obj2 or obj1[key]!=obj2[key]:
            flag=False
            break
    if flag:
        print("same")
    else:
        print("Not same")