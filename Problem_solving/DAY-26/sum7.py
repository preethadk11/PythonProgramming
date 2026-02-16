string="ABC".lower()
substring=[]
vowel="aeiou"
for i in range(len(string)):
    for j in range(i,len(string)):
        substring.append(string[i:j+1])
for word in substring:
    if word.startswith(tuple(vowel)):
        print(word)