n=[10,20,4,45,99]
first=n
maxi=first[0]
for i in range(len(first)):
  if first[i]>maxi:
    maxi=first[i]
first.remove(maxi)

print(max(first))