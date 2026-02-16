strings=input().split()
#print(max(strings,key=len))
largest=strings[0]
for word in strings:
    if len(word)>len(largest):
        largest=word
print(largest)