string="computer"
for i in range(len(string)):
    for j in range(len(string)-i):
        print(string[j],end="")
    print()