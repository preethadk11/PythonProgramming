string=input()
for start in range(len(string)):
    for end in range(start,len(string)):
        print(string[start:end+1])
        