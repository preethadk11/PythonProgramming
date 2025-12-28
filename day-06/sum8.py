words=["hello","everyone","preetha","is","good girl"]
max=words[0]

for i in words:
    if len(i)>len(max):
        max=i
print(max,len(max))
