names=["madhulakshmi","priyanga","preetha","kasthuri","doss","rajalakshi","anitha"]
count=0
vowel="aeiou"
for i in names:
    if i.startswith(tuple(vowel)):
        count+=1
print(count)