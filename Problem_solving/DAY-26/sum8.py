stringss="hello"

substring=[]

for i in range(len(stringss)):
  for j in range(i,len(stringss)):
    substring.append(stringss[i:j+1])
print(substring)
print(max(substring,key=len))