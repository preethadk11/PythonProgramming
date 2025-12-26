def count_vowels(string):
    count=0
    vowel="aeiou"
    for char in string.lower():
        if char in vowel:
            count+=1
    return count
string=input("Enter a string: ")
print(count_vowels(string))