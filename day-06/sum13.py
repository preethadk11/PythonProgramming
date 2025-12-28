def func(strings):
    strings.sort(key=len)
    return strings
strings=["apple","orange","banana","yello"]
print(func(strings))