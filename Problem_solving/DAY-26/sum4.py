string="ABCDE"
substring=[]
for i in range(len(string)):
    for j in range(i,len(string)):
        substring.append(string[i:j+1])
for i in substring:
    if len(i)==2:
        print(i)
