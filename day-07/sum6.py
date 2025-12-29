list1=[12,"apple","apple","23","23",12]
frequent=[]
for i in list1:
    if i not in frequent:
        frequent.append(i)
    elif i in frequent:
        count=list1.count(i)
        print(i,":",count)