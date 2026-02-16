string="xyz"
substring=[]
for i in range(0,1):
    for j in range(i,len(string)):
        substring.append(string[i:j+1])
print(substring)