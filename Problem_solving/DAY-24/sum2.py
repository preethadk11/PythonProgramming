n=[1,2,2,3,4,5,5,5,2]
dup=[]
for i in range(len(n)):
    if n[i] not in dup:
        dup.append(n[i])
print(dup)