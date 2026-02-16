string="abc"
substring=[]
for i in range(len(string)):
    
        substring.append(string[i:(len(string)-1)+1])
print(substring)