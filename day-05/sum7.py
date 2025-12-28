def remove_vowel(string):
    vowel="aeiou"
    strings=""
    for char in string:
        if char not in vowel:
            strings+=char
    print(strings)
string="hello everyone"
remove_vowel(string)
