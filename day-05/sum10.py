def remove_duplicate(string):
    duplicate=""
    for char in string:
        if char==" ":
            duplicate+=char
        elif char not in duplicate:
            duplicate+=char
    print(duplicate)
string="Hello everyone i am preetha"
remove_duplicate(string)