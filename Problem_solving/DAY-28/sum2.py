string=input()
vowel=tuple("aeiou")
vowel_count=0
consonent_count=0
for char in string:
    if char.isalpha():
       if char in vowel:
            vowel_count+=1
       else:
            consonent_count+=1
print(f'vowel count :{vowel_count} and consonent count :{consonent_count}')
