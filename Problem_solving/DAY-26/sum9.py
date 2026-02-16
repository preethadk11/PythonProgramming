string="abc"
substring=[]
for i in range(len(string),-1,-1):
    for j in range(i,len(string)):
        substring.append(string[i:j+1])
print(substring)